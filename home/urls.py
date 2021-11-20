from django.contrib import admin
from django.urls import path,include
from . import views
urlpatterns = [
    path('', views.index, name="index"),
    path('login',views.user_login, name="login"),
    path('dashboard',views.dashboard, name="dashboard"),
    path('results',views.results, name="results"),
]