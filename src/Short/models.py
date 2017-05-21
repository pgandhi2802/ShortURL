# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.forms import ModelForm

class ShortURL(models.Model):
	original_url = models.CharField(max_length=2000)
	token = models.CharField(max_length=15,unique=True)

	def __str__(self):
		return self.token
