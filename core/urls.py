from django.urls import path

from . import views

urlpatterns = [
    # path('rollcall', views.RollcallView.as_view(), name='rollcall'),
    path('', views.LoginView.as_view()),
    # path('login', views.LoginView.as_view(), name='login'),
    path('logout', views.logout_htmx),
    path('management', views.management_htmx),
    path('manage-current-rollcall', views.manage_current_roll_call_htmx),
    path('logout', views.logout_htmx),
    path('set-up-rollcall', views.RollCallSetUpView.as_view()),
    path('check-in', views.check_in_htmx),
    
]