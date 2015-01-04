from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from djangocup.models import Cup, Location
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.http import HttpResponse, HttpResponseRedirect

import datetime

# Create your views here.
def index(request):
	final_list = []
	cups_list = Cup.objects.all()[::-1]
	locs_list = Location.objects.all()
	

	return render(request, 'djangocup/index.html', {'cups_list':cups_list, 'locs_list':locs_list,})

def add_cup(request):

	location = get_object_or_404(Location,pk=request.POST['location'])
	c = Cup(lister_name=request.POST['name'], location=location, topic=request.POST['topic'], timestamp=timezone.now())
	c.save()
	return HttpResponseRedirect(reverse('index'))