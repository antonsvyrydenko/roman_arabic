# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
import json
import num_c # conversion module
from .models import Conversion

def index(request):
	return render(request, 'conv/index.html')

def convert(request):
	to_convert=request.GET['to_c']
	if 'to_c' in request.GET:
		if to_convert.isdigit():
			conversion_result = num_c.arabian_to_roman(int(to_convert))
		else:
			conversion_result = num_c.roman_to_arabian(to_convert)

	json_string={"to_c": to_convert, "conv": conversion_result }
		
	new_conversion=Conversion.objects.create(
		entry_to_convert=to_convert,
		converted_entry=conversion_result)

	return render(request, 'conv/index.html', {'json':json.dumps(json_string)})