from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    path('', views.agung, name='Agung'),
    url('SIGN-UP', views.register, name='Register'),
    url('LOGIN', views.Login, name='Login')
]
