from django.urls import path

from . import views

urlpatterns = [
    # path('rollcall', views.RollcallView.as_view(), name='rollcall'),
    path('', views.LoginView.as_view()),
    # path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_htmx),
    path('rollcall-form', views.rollcall_form),
    path('set-up-rollcall', views.set_up_rollcall_form),
    
]