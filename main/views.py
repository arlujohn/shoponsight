from django.shortcuts import render
from django.http import HttpResponse
from . import utils
# Create your views here.

def main_page(response):
    return HttpResponse(utils.welcome_user("Arlu John"))

def home(response):
    return render(response,"main/home.html",{})

def register(response):
    return render(response,"main/register.html",{})