from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User

def entrada(request):
    return render(request, "TchaugenteApp/entrada.html")
