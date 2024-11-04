from django.shortcuts import render
from django.views.generic import TemplateView




class AddMoneyView(TemplateView):
    template_name = 'add-money-page.html'

class LoginView(TemplateView):
    template_name = 'login-page.html'

class ProfileView(TemplateView):
    template_name = 'profile-page.html'

class RegistrationView(TemplateView):
    template_name = 'registration-page.html'

class TransactionView(TemplateView):
    template_name = 'transaction-page.html'