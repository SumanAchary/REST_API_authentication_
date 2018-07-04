# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from rest_framework import serializers


class users_details(models.Model):
 	username = models.CharField(max_length = 25,null = True, blank = True )
 	Email = models.EmailField(max_length = 50,unique = True)
 	Phone = models.CharField(max_length = 11)
 	password = models.CharField(max_length = 16,null = True, blank = True)
	otp =  models.CharField(max_length = 10,null = False, blank = True)
	is_activate = models.BooleanField(default=False)




