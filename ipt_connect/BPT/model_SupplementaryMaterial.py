# coding: utf8

from django.db import models

from .models import Team, Problem


class SupplementaryMaterial(models.Model):
    team = models.ForeignKey(Team, null=True,on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    link = models.CharField(max_length=5000)
