# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,get_object_or_404
from django.http import HttpResponseRedirect
from .models import ShortURL
import urllib2
import random
import string
from  ShortURL import settings
def check_if_url_works(url):
	try:
		urllib2.urlopen(url)
		return True
	except:
		return False

def get_token():
	_token = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(random.randint(8,15)))
	print ("inside get_token:{}".format(_token))
	try:
		_object = get_object_or_404(ShortURL,token=_token)
		_token = get_token()
	except:
		return _token
	return _token


def index(request,in_token=""):
	print (settings.BASE_DIR)
	url_link=request.POST.get('url_link')
	print(url_link)
	context = {}
	if in_token == "":
		if url_link == None:
			context = {
				'error_flag': False,
				'generation_flag': False,
			}
		elif check_if_url_works(url_link):
			try:
				print(","+url_link+",")
				_object = get_object_or_404(ShortURL,original_url=url_link)
				print("Already Exist")
				context = {
					'error_flag': False,
					'generation_flag': True,
					'generated_url': request.build_absolute_uri()+_object.token
				}
				print(context)
			except:
				_token = get_token()
				shorturl_obj=ShortURL(original_url=url_link,token=_token)
				shorturl_obj.save()
				context = {
					'error_flag':False,
					'generation_flag': True,
					'generated_url': request.build_absolute_uri()+_token
				}
				print(context)
		else:
			context = {
				'generation_flag': False,
				'error_flag': True,
				'error_message': 'This URL doesn\'t seem to be working',
			}
			print(context)
	else:
		try:
			_object = get_object_or_404(ShortURL,token=in_token)
			print(_object.original_url)
			return HttpResponseRedirect(_object.original_url)
		except:
			context = {
				'generation_flag': False,
				'error_flag': True,
				'error_message': 'Provided token is not attached with any of the URL'
			}
	return render(request,'Short/index.html',context)