from django.conf.urls import patterns, include, url
from views import HomePageView

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    url(r'^$', HomePageView.as_view(), name='home'),
    url(r'^cashflow/', include('cashflow.urls')),


    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),
)
