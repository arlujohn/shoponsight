from django.urls import path
from . import views

urlpatterns = [
    #path("home/", views.main_page,name="main_page"),
    path("home/", views.home,name="home"),
    path("login/", views.login,name="login"),
    path("register/", views.register,name="register"),
]