from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask_Semenchenko.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_Semenchenko.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main, name = 'main page'),
    url('^hello/$', hello),
    url('^postget/$', postget),
    url('^myHello/$', myHello),
)
