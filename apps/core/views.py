from django.shortcuts import render_to_response
from django.http import HttpResponse
from django.template import RequestContext 

#from apps.core.models import Torneo, Problema, Solucion


def index(request):
	return render_to_response('home.html', {'title': 'Inicio','user': request.user},context_instance=RequestContext(request))
