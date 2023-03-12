from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.views.generic import CreateView
from .forms import UserRegistrationForm


class UserRegistrationView(CreateView):
    form_class = UserRegistrationForm
    success_url = reverse_lazy('login')
    template_name = 'user/signup.html'
    success_message = "Your Account Has Been Registered, Please LogIn Now To Create Amazing Articles."
