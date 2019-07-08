# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length = 20)
    email = models.EmailField(max_length = 40)
    mobile = models.CharField(unique=True, max_length=10)
    age = models.IntegerField()
    profession = models.CharField(max_length = 40)

    def __str__(self):
        return self.name

class CustomerFamily(models.Model):
    Relation = (('Sister','Sister'),
                ('Brother','Brother'),
                ('Father','Father'),
                ('Mother','Mother'))
    family = models.ForeignKey(Customer, related_name='family', on_delete=models.CASCADE)
    relation = models.CharField(choices=Relation,max_length=15)
    name = models.CharField(max_length = 20)
    email = models.EmailField()
    mobile = models.CharField(unique=True, max_length=10)
    age = models.IntegerField()
    profession = models.CharField(max_length = 40)