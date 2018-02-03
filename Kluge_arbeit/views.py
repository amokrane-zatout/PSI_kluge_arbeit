# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
#from form import *


def index(request):
    return render(request, "user.html")

def login(request):
    if request.method == 'POST':
       # print"je ss dans le login"
        username = request.POST['username']
        password = request.POST['password']
        #print username
        # user = authenticate(request, username=username, password=password)
        if username == "admin" and password == "admin":
            # login(request, user)
            return render(request, "user.html")
    return render(request, "login.html")


def chapitre(request):
    return render(request, "chapitres.html")

def dashboard(request):
    return render(request, "dashboard.html")

def table(request):
    return render(request, "table.html")

def addMatiere(request):
    return render(request, "addMatiere.html")


def addChapitre(request):
    return render(request, "addChap.html")


def modifMatiere(request) :
    return render(request, "modifMatiere.html")

def supprimMatiere(request) :
    return render(request, "deleteMatiere.html")

def modifChapitre(request) :
    return render(request, "modifChap.html")

def supprimChapitre(request) :
    return render(request, "deleteChap.html")

def timer(request) :
    return render(request, "seanceRevision.html")


def feedBack(request) :
    return render(request, "feedback.html")

def abandonSeance(request):
    return render(request, "abandonSeance.html")

