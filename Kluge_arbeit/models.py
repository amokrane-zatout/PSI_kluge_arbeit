# -*- coding: utf-8 -*-


from django.db import models

class Utilisateur(models.Model):

  password = models.CharField(max_length=200)
  nom = models.CharField(max_length=200)
  prenom = models.CharField(max_length=200)
  mail = models.CharField(max_length=200)
  filiere = models.CharField(max_length=200)
  tps_concentration = models.IntegerField()
  ordre_travail = models.IntegerField()
  fiche_lecture = models.IntegerField()
  start_difficult = models.IntegerField()
  start_preference = models.IntegerField()
  tps_pause = models.IntegerField()
  supplementaire = models.IntegerField()

class Matiere (models.Model):
  libelle = models.CharField(max_length=200)
  degre_difficult = models.IntegerField()
  degre_preference = models.IntegerField()
  note_esperee = models.FloatField()
  utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null = True)
class Seance(models.Model):
  date = models.DateField('date published')
  heureDebut = models.DateTimeField()
  heureFin = models.DateTimeField()
  utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, null = True)
  matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null = True)


  
class Chapitre (models.Model):
  libelle_chapitre = models.CharField(max_length=200)
  acquis = models.BooleanField()
  progression = models.FloatField()
  matiere = models.ForeignKey(Matiere, on_delete=models.CASCADE, null = True)
