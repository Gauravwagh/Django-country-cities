from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    url(r'^home/', include('home.urls')),
    url(r'^cities_light/api/', include('cities_light.contrib.restframework3')),
    url(r'^admin/', include(admin.site.urls)),
)
