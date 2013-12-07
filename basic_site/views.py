from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext, loader
from django.conf import settings
from basic_site.models import Interest
import requests
import pprint

# Create your views here.

def index(request):

	error_message = "";

	#get request
	if request.method == 'GET':
		template = loader.get_template('splash.html')

	#post request
	elif request.method == 'POST':
		template = loader.get_template('splash_confirm.html')
		email = request.POST.get('email', '')
		if (email != ''):
			interest = Interest(email=email)
			interest.save()

	context = RequestContext(request, {
		'error_message': error_message,
	})

	return HttpResponse(template.render(context))