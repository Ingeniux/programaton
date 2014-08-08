from django.shortcuts import render_to_response, HttpResponse
from django.core.context_processors import csrf
from django.template import RequestContext 


from apps.challenges.forms import ChallengeForm


def index(request):
	return HttpResponse("Challenges")

def challenge_index(request, challenge_id):
	#torneo = Torneo.objects.get(id=id)
	#soluciones = Solucion.objects.filter(torneo=id)
	#return render_to_response('realtime.html', {'torneo': torneo, 'soluciones': soluciones}, context_instance=RequestContext(request))
	return HttpResponse("Realtime %s" % challenge_id)


def challenge_details(request, challenge_id):
	#torneo = Torneo.objects.get(pk=id)
	#return render_to_response('challenge_details.html', {'torneo': torneo, 'problemas': problemas }, context_instance=RequestContext(request))
	return HttpResponse("Detalles %s" % challenge_id)


def challenge_list(request):
	#torneos = Torneo.objects.all().order_by('-fecha_inicio')
	#return render_to_response('torneos.html', {'torneos': torneos}, context_instance=RequestContext(request))
	return HttpResponse("Listado")

	

def challenge_register(request):
    if request.POST:
        form = ChallengeForm(request.POST)
        if form.is_valid:
            form.save()
 
            return HttpResponseRedirect('/')
    else:
        form = ChallengeForm()
     
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    args['title'] = 'Crer torneo'
 
    return render_to_response('challenge_register.html', args, context_instance=RequestContext(request))
	