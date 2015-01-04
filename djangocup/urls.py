from django.conf.urls import patterns, url
from djangocup import views

urlpatterns = patterns('',
	url(r'^add/?',views.add_cup,name='add'),
	)