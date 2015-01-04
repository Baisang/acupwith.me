from django.conf.urls import patterns, include, url
from django.contrib import admin

from djangocup import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'djangocup.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index,name='index'),
    url(r'^', include('djangocup.urls')),
    # url(r'^$', views.index, name="index"),
)
