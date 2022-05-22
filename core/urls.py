from django.urls import path

from . import views

urlpatterns = [
    path('rollcall', views.RollcallView.as_view(), name='rollcall'),
    path('', views.SplashView.as_view(), name='splash'),
]