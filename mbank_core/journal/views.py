from django.contrib.auth.models import User
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from journal.models import CustomUser
from typing import Any
from django.db import transaction
from django.contrib.auth import login
from django.views.generic import TemplateView, View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password

class AddMoneyView(TemplateView):
    template_name = 'add-money-page.html'
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = {
            'current_user': current_user
        }

        return context

class AddMoneyClickView(TemplateView):
    template_name = 'add-money-page.html'
    def get_context_data(self, **kwargs):
        current_user = self.request.user

        current_user.balance += 1
        current_user.save()
        context = {
            'current_user': current_user
        }
        return context

class LoginView(TemplateView):
    template_name = 'login-page.html'




class MakeLoginView(View):
    def post(self, request, *args, **kwargs):
        phone_number = self.request.POST.get('phone')
        password = self.request.POST.get('password')

        try:
            user = User.objects.get(phone_number=phone_number)
        except:
            return render(request, template_name='registration-page.html', context={'current_user': self.request.user})

        if check_password(password, user.password):
            login(self.request, user)
            return render(request, template_name='profile-page.html', context={'current_user': self.request.user})

        else:
            return render(request, template_name='registration-page.html', context={'current_user': self.request.user})


class ProfilePageView(TemplateView):
    template_name = "profile-page.html"

    def get_context_data(self, **kwargs: Any):
        curent_user = self.request.user

        context = {
            'current_user': curent_user
        }

        return context
class ProfileView(TemplateView):
    template_name = 'profile-page.html'
    def get_context_data(self, **kwargs):
        current_user = self.request.user
        context = {
            'current_user': current_user
        }
        return context

class RegistrationView(TemplateView):
    template_name = 'registration-page.html'

    def post(self, request, *args, **kwargs):
        username = self.request.POST.get('name')
        phone_number = self.request.POST.get('phone')
        password = self.request.POST.get('password')

        if not username or not phone_number or not password:
            print(username, phone_number, password)
            render(request, template_name='profile-page.html')

        user = User(username=username, phone_number=phone_number)
        user.password = make_password(password=password)

        try:
            user.save()
        except:
            return render(request, template_name='login-page.html', context={'current_user': self.request.user})
        login(self.request, user)
        context = {
            'current_user': self.request.user
        }

        print('Work')
        return render(request, template_name='profile-page.html', context=context)

class TransactionView(TemplateView):
    template_name = 'transaction-page.html'



class MakeTransactionView(View):
    def post(self, request, *args, **kwargs):
        sendler = request.user
        receiver_number = request.POST.get('phone')
        amount = request.POST.get('amount')

        context = {
            'current_user': sendler
        }

        try:
            receiver = User.objects.get(phone_number=receiver_number)
        except User.DoesNotExist:
            return render(request, template_name='profile-page.html', context=context)

        amount = float(amount)

        try:
            if amount >= 1 and sendler.balance >= amount and not (sendler.phone_number == receiver.phone_number):
                sendler.balance -= amount
                receiver.balance += amount
        except:
            return render(request, template_name='registration-page.html', context=context)

            with transaction.atomic():
                sendler.save()
                receiver.save()

            return render(request, template_name='profile-page.html', context=context)

