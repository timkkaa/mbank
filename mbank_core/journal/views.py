from django.contrib.auth import authenticate, login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.models import User
from django.db import transaction
from django.http import HttpResponse, Http404
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView

from journal.models import CustomUser


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

    def login_view(request):
        if request.method == 'POST':
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            # Аутентификация пользователя
            user = authenticate(request, username=phone, password=password)

            if user is not None:
                # Логиним пользователя и перенаправляем на главную страницу
                login(request, user)
                return redirect('home')  # Замените 'home' на нужный URL

            # Ошибка аутентификации
            return HttpResponse("Неправильный номер телефона или пароль")

        # Показ формы логина, если метод запроса не POST
        return render(request, 'login-page.html')

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
    def register_view(request):
        if request.method == 'POST':
            name = request.POST.get('name')
            phone = request.POST.get('phone')
            password = request.POST.get('password')

            # Проверяем, существует ли пользователь с таким номером телефона
            if User.objects.filter(username=phone).exists():
                return HttpResponse("Пользователь с таким номером телефона уже существует")

            # Создаем нового пользователя
            user = User.objects.create(
                username=phone,
                first_name=name,
                password=make_password(password)  # Хэшируем пароль
            )

            # После успешной регистрации можно перенаправить пользователя на страницу логина
            return redirect('login')

        # Отображаем форму регистрации, если метод запроса не POST
        return render(request, 'registration-page.html')



class TransactionView(TemplateView):
    template_name = 'transaction-page.html'



class MakeTransactionView(View):
    def post(self, request, *args, **kwargs):
        input_data = request.POST
        phone_number_value = input_data['phone']
        amount = input_data['amount']

        try:
            receiver = CustomUser.objacts.get(phone_number_value=phone_number_value)

        except CustomUser.DoesnotExist:
            raise Http404

        sender = request.user

        amount = float(amount)
        if sender.balance < amount:
            return HttpResponse('У вас недостаточно средства!')

        with transaction.atomic():
            sender.profile.balance -= amount
            receiver.profile.balance += amount
            sender.profile.save()
            receiver.profile.save()

        return redirect('my-profile-url')
