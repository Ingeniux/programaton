from django.shortcuts import render_to_response, render
from django.http import HttpResponse, HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required

from django.template import RequestContext 
from django.core.context_processors import csrf

from apps.accounts.forms import FrikiForm, FrikiChangeForm


def index(request):
	return render_to_response('friki_index.html', {'title': 'Cuentas'}, context_instance=RequestContext(request))

def friki_register(request):
    if request.POST:
        form = FrikiForm(request.POST)
        if form.is_valid:
            form.save()
 
            return HttpResponseRedirect('/')
    else:
        form = FrikiForm()
     
    args = {}
    args.update(csrf(request))
    
    args['form'] = form
    args['title'] = 'Registro'
 
    return render_to_response('friki_register.html', args, context_instance=RequestContext(request))

def friki_login(request):
	if  request.method == 'POST':
		form = AuthenticationForm(data=request.POST)
		if form.is_valid():
			email = form.cleaned_data['username']
			password = form.cleaned_data['password']
			user = authenticate(username=email, password=password)
			if user is not None and user.is_active:
				login(request,user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse('Algo salio mal')
		else:
			return HttpResponse('El formulario no es valido')
	else:
		form = AuthenticationForm()
		ctx = {'form': form, 'title': 'Login'}
		return render(request, 'friki_login.html', ctx, context_instance=RequestContext(request))

@login_required(login_url='/user/login/')
def friki_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


@login_required(login_url='/user/login/')
def friki_update(request):
    if request.POST:
        form = FrikiChangeForm(request.POST)
        if form.is_valid:
            form.save()
 
            return HttpResponseRedirect('/')
    else:
        form = FrikiChangeForm(initial={'alias': request.user.alias, 'email': request.user.email, 'password': ""})
     
    args = {'user': request.user}
    args.update(csrf(request))
    
    args['form'] = form

 
    return render_to_response('register_friki.html', args)