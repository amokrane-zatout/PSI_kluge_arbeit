# -*- coding: utf-8 -*-


from django.db import models

class Utilisateur(models.Model):
    id_utilisateur = models.CharField(max_length=50,null=True, blank=True)
    name=models.CharField(max_length=100000,null=True, blank=True)


