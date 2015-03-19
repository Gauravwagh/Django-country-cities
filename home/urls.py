from django.conf.urls import patterns, url

urlpatterns = patterns('home.views',
                        #url(r'^invoice_generate/(?P<invid>\d+)$', 'invoice_generate'),
                        url(r'^getregion/(?P<contryid>\d+)$', 'getregion'),
                        url(r'^getrcity/(?P<regionid>\d+)$', 'getrcity'),
                       )