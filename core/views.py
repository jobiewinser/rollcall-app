from datetime import datetime
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
    # return redirect('/')
    # return redirect('login')

def logout_htmx(request):
    logout(request)
    return redirect('/')

def check_in_htmx(request):
    
    rollcall_pk = request.POST.get('rollcall', '')
    rollcall = RollCall.objects.get(pk=rollcall_pk)
    person_pk = request.POST.get('person', '')
    person = Person.objects.get(pk=person_pk)
    people_with_you_pk_list = request.POST.getlist('people_with_you')
    people_with_you = Person.objects.filter(pk__in=people_with_you_pk_list)
    further_details = request.POST.get('further_details', '')
    
    checkin = CheckIn.objects.create(rollcall=rollcall, person=person, further_details=further_details)
    checkin.people_with_you.set(people_with_you)
    checkin.save()
    return redirect('/')

def management_htmx(request):
    if request.META.get("HTTP_HX_REQUEST") != 'true':
        return render(request, 'management.html_full', {})
    return render(request, 'management.html', {})
def manage_current_roll_call_htmx(request):
    context = {}
    current_rollcalls = RollCall.objects.filter(started__lte=datetime.now(), closed=False)
    if current_rollcalls:
        context['current_rollcall'] = current_rollcalls.latest()

    for item in context['current_rollcall'].checkin_rollcall.all():
        print(item)

    if request.META.get("HTTP_HX_REQUEST") != 'true':
        return render(request, 'manage_current_roll_call_full.html', context)
    return render(request, 'manage_current_roll_call.html', context)

class RollCallSetUpView(View):
    def get(self, request):
        if request.META.get("HTTP_HX_REQUEST") != 'true':
            return render(request, 'set_up_rollcall_form_full.html', {})
        return render(request, 'set_up_rollcall_form.html')
    def post(self, request):
        current_rollcalls = RollCall.objects.filter(started__lte=datetime.now(), closed=False)
        if not current_rollcalls:
            now_or_schedule = request.POST.get('now_or_schedule', '')
            if now_or_schedule == 'now':
                started = datetime.now()
            else:
                started = datetime.strptime(request.POST.get('started', ''), '%Y-%m-%dT%H:%M').date()
            new_rollcall = RollCall(started=started)
            new_rollcall.save()
        print()
        return redirect('/')



class LoginView(LoginView):
    template_name = 'index.html'
    success_url = "/"
    form_class = UserLoginForm
    success_message = "Successful Login"
    def get_context_data(self, **kwargs):
        kwargs['current_rollcalls'] = RollCall.objects.filter(started__lte=datetime.now(), closed=False)
        kwargs['current_rollcall'] = kwargs['current_rollcalls'].latest()
        # kwargs['user_checkin'] = CheckIn.objects.filter(person=datetime.now(), closed=False) MAYBE SESSION?
        kwargs['people'] = Person.objects.all()
        
        return super().get_context_data(**kwargs)

class LogoutView(View):
    def get(self, request):
        logout(request)
        return HttpResponseRedirect("/")