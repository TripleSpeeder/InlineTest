from django.conf.urls import patterns, include, url

from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^pizza/', include('pizza.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
