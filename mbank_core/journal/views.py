from django.shortcuts import render
from django.views.generic import TemplateView




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


class TransactionView(TemplateView):
    template_name = 'transaction-page.html'
