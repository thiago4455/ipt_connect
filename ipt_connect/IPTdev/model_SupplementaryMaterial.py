# coding: utf8

from django.db import models

from . import models as ipt_connect_models


class SupplementaryMaterial(models.Model):
    team = models.ForeignKey(ipt_connect_models.Team, null=True, on_delete=models.CASCADE)
    problem = models.ForeignKey(ipt_connect_models.Problem, on_delete=models.CASCADE)
    name = models.CharField(max_length=500)
    link = models.CharField(max_length=5000)
