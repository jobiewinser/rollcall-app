from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import View, TemplateView
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin
from django.conf import settings
from django.views.generic.edit import CreateView, UpdateView
from .models import *
from django.shortcuts import get_object_or_404
from django.urls import reverse
from .forms import *
from django.core.mail import EmailMessage
from django.db.models import Q

# class LoginView(SuccessMessageMixin, LoginView):
#     template_name = 'login.html'
#     success_url = "/management"
#     form_class = UserLoginForm
#     success_message = "Successful Login"

# class RollcallView(TemplateView):
#     template_name = "rollcall.html"

# class SplashView(TemplateView):
#     template_name = "splash.html"


# def index(request):
    # if request.user.is_authenticated:
    # return render(request, 'index.html')
    # return redirect('login')

def logout_htmx(request):
    logout(request)
    return render(request, 'index.html')

def rollcall_form(request):    
    return render(request, 'rollcall_form.html')

def set_up_rollcall_form(request):    
    if request.META.get("HTTP_HX_REQUEST") != 'true':
        # return redirect('index')
        return render(request, 'set_up_rollcall_form_full.html', {})

    return render(request, 'set_up_rollcall_form.html')

class LoginView( LoginView):
    template_name = 'index.html'
    success_url = "/"
    form_class = UserLoginForm
    success_message = "Successful Login"

class LogoutView(View):
    def get(self, request):
        return HttpResponseRedirect("/")

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")