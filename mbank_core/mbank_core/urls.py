"""
URL configuration for mbank_core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from journal.views import (AddMoneyView, LoginView,
                           ProfileView, RegistrationView,
                           TransactionView, AddMoneyClickView,
                           MakeTransactionView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('add-money/', AddMoneyView.as_view()),
    path('add-money/', AddMoneyClickView.as_view(), name='click-button-url'),
    path('login/', LoginView.as_view(), name='login-url'),
    path('profile/', ProfileView.as_view(), name='profile-url'),
    path('registration/', RegistrationView.as_view(), name='registration-url'),
    path('transaction/', TransactionView.as_view()),
    path('transaction/', MakeTransactionView.as_view(), name='transaction-url'),

]
