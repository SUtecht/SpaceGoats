# Create your views here.
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from demo.models import *
from django.http import Http404
from django.utils import timezone
from dateutils import relativedelta
import datetime
from django.core import serializers

def eventsJson(request):
	month_start = datetime.datetime(timezone.now().year, timezone.now().month, 1, 0)
	next_month = month_start+relativedelta(months=+1)
	month_end = next_month+relativedelta(seconds=-1)
	
	data = serializers.serialize("json", Event.objects.all())
	return HttpResponse(data, content_type="text/plain")

def index(request):
	if request.method == 'POST':
		event_form = EventForm(request.POST)
		if event_form.is_valid():
			name = event_form.cleaned_data['name']
			type = event_form.cleaned_data['type']
			begin = event_form.cleaned_data['begin']
			end = event_form.cleaned_data['end']
			completed = 'N'
			
			new_event = Event(name=name, type=type,begin=begin, end=end, completed=completed)
			new_event.save()
			print('event created')
	
	current_terms = Term.objects.filter(begin__lte=timezone.now(), end__gte=timezone.now())
	pools_in_term = {}
	for  t in current_terms:
		pools_in_term[t] = Pool.objects.filter(term = t)
	event_form = EventForm()
	return render_to_response('demo/index.html', {'event_form':event_form,
													'pools_in_term':pools_in_term,
													'current_terms':current_terms,
													'timezone':timezone},
													context_instance=RequestContext(request))
	
