from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from .admin import UserCreationForm
from .models import *
from django.shortcuts import get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, 'index.html')


def profile(request):
    return render(request, 'user/profile.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('customauth:login_view')
    template_name = 'registration/signup.html'
