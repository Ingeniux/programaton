from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'apps.core.views.index'),
    url(r'^manager/', include(admin.site.urls)),
    url(r'^accounts/', include('apps.accounts.urls')),
    url(r'^challenges/', include('apps.challenges.urls')),

)
