from genericpath import exists
from django.shortcuts import render, redirect
from .models import UserModel
from django.http import HttpResponse
from django.contrib.auth import get_user_model
from django.contrib import auth

# Create your views here.

    


def index_view(request):
    if request.method =='GET':
        return render(request, 'user/index.html')  


    
