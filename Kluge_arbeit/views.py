# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse

from .models import *
from .forms import updateProfilForm
from django.contrib.auth import authenticate, login, logout
#from form import *



import pandas

from sklearn import model_selection
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.naive_bayes import GaussianNB
from sklearn.svm import SVC

def index(request, utilisateur_id):
    utilisateur = get_object_or_404(Utilisateur, pk=utilisateur_id)
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        utilisateur.nom = request.POST.get('nom', utilisateur.nom)
        utilisateur.prenom = request.POST.get('prenom', utilisateur.nom)
        utilisateur.mail = request.POST.get('mail', utilisateur.mail)
        utilisateur.filiere = request.POST.get('filiere', utilisateur.filiere)

        utilisateur.tps_concentration = request.POST.get('tmpsConcentration', utilisateur.tps_concentration)
        utilisateur.fiche_lecture = request.POST.get('fichelecture', utilisateur.fiche_lecture)
        utilisateur.ordre_travail = request.POST.get('ordre', utilisateur.ordre_travail)
        utilisateur.start_difficult = request.POST.get('difficulte', utilisateur.start_difficult)
        utilisateur.start_preference = request.POST.get('preference', utilisateur.start_preference)
        utilisateur.supplementaire = request.POST.get('supplimentaires', utilisateur.supplementaire)


        utilisateur.save()
        print(request.POST.get('fichelecture', utilisateur.fiche_lecture))
        return render(request, "Kluge_arbeit/user.html", {'utilisateur_id': utilisateur_id, 'utilisateur':utilisateur})

        # if a GET (or any other method) we'll create a blank form





    return render(request, "Kluge_arbeit/user.html", {'utilisateur_id' : utilisateur_id, 'utilisateur':utilisateur})

def login(request):
    if request.method == 'POST':
       # print"je ss dans le login"
        username = request.POST['username']
        password = request.POST['password']



        try:
            utilisateur = get_object_or_404(Utilisateur, mail=username, password=password)
        except :
            # Redisplay the question voting form.
            return render(request, 'Kluge_arbeit/login.html', {

                'error_message': "login ou mot de passe incorrect",
            })
        else:



            return HttpResponseRedirect(reverse('index', args=(utilisateur.id,)))

    return render(request, "Kluge_arbeit/login.html")


def chapitre(request):

    chapitres = Chapitre.objects.all()

    return render(request, "Kluge_arbeit/chapitres.html", {'chapitres': chapitres})

def dashboard(request):
    return render(request, "Kluge_arbeit/dashboard.html")

def table(request, utilisateur_id):

    matiere_list = Matiere.objects.filter(utilisateur__id=utilisateur_id)
    context = {'matiere_list': matiere_list, 'utilisateur_id' : utilisateur_id}

    return render(request, "Kluge_arbeit/table.html", context)

def addMatiere(request, utilisateur_id):

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        libelle = request.POST.get('libelle')
        degre_difficult = request.POST.get('degDiff')
        degre_preference = request.POST.get('degPref')
        note_esperee = request.POST.get('note')
        utilisateur_id=utilisateur_id
        matiere = Matiere.objects.create(libelle=libelle, degre_difficult=degre_difficult, degre_preference=degre_preference, utilisateur_id=utilisateur_id, note_esperee=note_esperee)
        matiere.save()
        return HttpResponseRedirect(reverse('table', args=(utilisateur_id,)))
    return render(request, "Kluge_arbeit/addMatiere.html", {'utilisateur_id':utilisateur_id})


def addChapitre(request, matiere_id, utilisateur_id):

    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        libelle_chapitre = request.POST.get('libelle_chapitre')
        acquis = request.POST.get('acquis')
        progression = request.POST.get('progression')

        chapitre = Chapitre.objects.create(libelle_chapitre=libelle_chapitre, acquis=acquis, progression=progression, matiere_id=matiere_id)
        chapitre.save()
        return HttpResponseRedirect(reverse('chapitre'))
    return render(request, "Kluge_arbeit/addChap.html", {'matiere_id':matiere_id, 'utilisateur_id':utilisateur_id})


def modifMatiere(request, matiere_id, utilisateur_id) :
    matiere = get_object_or_404(Matiere, pk=matiere_id)
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        matiere.libelle = request.POST.get('libelle')
        matiere.degre_difficult = request.POST.get('degDiff')
        matiere.degre_preference = request.POST.get('degPref')
        matiere.note_esperee = request.POST.get('note')

        matiere.save()
        return HttpResponseRedirect(reverse('table', args=(utilisateur_id,)))
    return render(request, "Kluge_arbeit/modifMatiere.html", {'utilisateur_id':utilisateur_id, 'matiere': matiere})


def supprimMatiere(request, matiere_id, utilisateur_id) :
    matiere = get_object_or_404(Matiere, pk=matiere_id)
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:

        matiere.delete()
        return HttpResponseRedirect(reverse('table', args=(utilisateur_id, )))


    return render(request, "Kluge_arbeit/deleteMatiere.html", {'utilisateur_id':utilisateur_id, 'matiere': matiere})

def modifChapitre(request, chapitre_id) :
    chapitre = get_object_or_404(Chapitre, pk=chapitre_id)
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:
        chapitre.libelle_chapitre = request.POST.get('libelle_chapitre')
        chapitre.acquis = request.POST.get('acquis')
        chapitre.progression = request.POST.get('progression')


        chapitre.save()
        return HttpResponseRedirect(reverse('chapitre'))
    return render(request, "Kluge_arbeit/modifChap.html", {'chapitre': chapitre})

def supprimChapitre(request, chapitre_id) :
    chapitre = get_object_or_404(Chapitre, pk=chapitre_id)
    if request.method == 'POST':

        # create a form instance and populate it with data from the request:

        chapitre.delete()
        return HttpResponseRedirect(reverse('chapitre'))


    return render(request, "Kluge_arbeit/deleteChap.html", {'chapitre' : chapitre_id})

def timer(request) :
    return render(request, "Kluge_arbeit/seanceRevision.html")


def feedBack(request) :
    return render(request, "Kluge_arbeit/feedback.html")

def abandonSeance(request):
    return render(request, "Kluge_arbeit/abandonSeance.html")