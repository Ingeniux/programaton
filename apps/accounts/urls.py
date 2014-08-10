from django.conf.urls import patterns, url
from apps.accounts import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
	url(r'^register/', views.friki_register, name='register'),
    url(r'^login/', views.friki_login, name='login'),
    url(r'^logout/', views.friki_logout, name='logout'),
    url(r'^update/', views.friki_update, name='update'),
	)