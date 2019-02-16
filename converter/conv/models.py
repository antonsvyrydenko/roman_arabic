# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.

class Conversion(models.Model):
	entry_to_convert=models.CharField(max_length=30)
	converted_entry=models.CharField(max_length=30)