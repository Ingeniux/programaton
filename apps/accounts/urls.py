from django.conf.urls import patterns, url
from apps.accounts import views

urlpatterns = patterns('',
	url(r'^$', views.index, name='friki_index'),
	url(r'^register/', views.friki_register, name='friki_register'),
    url(r'^login/', views.friki_login, name='friki_login'),
    url(r'^logout/', views.friki_logout, name='friki_logout'),
    url(r'^update/', views.friki_update, name='friki_update'),
	)