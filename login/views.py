from django.shortcuts import render
from django.http import HttpResponse
from .forms import LoginNewList

# Create your views here.
def login(response):
    form = LoginNewList()
    return render(response,"login/login.html",{"form":form})