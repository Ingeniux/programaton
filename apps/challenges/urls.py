from django.conf.urls import patterns, url
from apps.challenges import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='challenges_index'),
	url(r'^(?P<challenge_id>\d+)/', views.challenge_index, name='challenge'),
	url(r'^details/(?P<challenge_id>\d+)/', views.challenge_details, name='challenge_details'),
	url(r'^list/', views.challenge_list, name='challenge_list'),
	url(r'^register/', views.challenge_register, name='challenge_register'),	
	)