from django.conf.urls import patterns, include, url
from django.contrib import admin
from ask.views import *
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask_Semenchenko.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', main, name='main page'),
    url(r'^ask/$', ask, name='asking'),
    url(r'^question/(\d+)/$', question, name='question'),
    url(r'^login/$', login, name='login'),
    url(r'^register/$', register, name='register'),
    url(r'^image/$', image, name='abTesting'),
    url('^hello/$', hello),
    url('^postget/$', postget),
    url('^myHello/$', myHello),
    url('^tag/(\d+)/$', tag, name='tag'),
)