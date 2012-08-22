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

	current_terms = Term.objects.filter(begin__lte=timezone.now(), end__gte=timezone.now())
	pools_in_term = {}
	for  t in current_terms:
		pools_in_term[t] = Pool.objects.filter(term = t)
	
		
	if request.method == 'POST':
		print('\n I see the post! \n ')
		event_form = EventForm(request.POST)
		if event_form.is_valid():
			print('\n Valid Event! \n')
			name = event_form.cleaned_data['name']
			begin_date = event_form.cleaned_data['begin_date']
			end_date = event_form.cleaned_data['end_date']
			begin_time = event_form.cleaned_data['begin_time']
			end_time = event_form.cleaned_data['end_time']
			completed = 'N'
			
			begin = begin_date+ ' ' + begin_time
			end = end_date + ' ' + end_time
			
			print(end)
			
			new_event = Event(name=name, begin=begin, end=end, completed=completed)
			new_event.save()
			print('\n Event created!\n')
			event_form = EventForm()
		else:
			print(event_form.errors)
	else:		
		event_form = EventForm()
		
	return render_to_response('demo/index.html', {'event_form':event_form,
													'pools_in_term':pools_in_term,
													'current_terms':current_terms,
													'timezone':timezone},
													context_instance=RequestContext(request))
	
def pool_view(request,pool_id):
	members_of_this_pool = Pool_Member.objects.filter(pool=pool_id)
	count = {0:members_of_this_pool.filter(status=0).count(), 1:members_of_this_pool.filter(status=1).count()}
	pool = Pool.objects.get(pk=1)
	return render_to_response('demo/pool_view.html', {'members_of_this_pool':members_of_this_pool,
													'pool':pool,
													'count':count},
													context_instance=RequestContext(request))
														
def pool_member(request,voter_id):
	this_voter = Voter.objects.get(pk=voter_id)
	member = Pool_Member.objects.filter(voter= this_voter)[0]
	return render_to_response('demo/pool_member.html', {'member':member,
													'voter':this_voter},
													context_instance=RequestContext(request))
													
def event(request, event_id):
	event = Event.objects.get(pk=event_id)
	new_pool_form = NewPoolForm()
	old_pool_form = OldPoolForm()
	return render_to_response('demo/events.html', {'event':event,
												'timeszone':timezone,
												'new_pool_form':new_pool_form,
												'old_pool_form':old_pool_form},
												context_instance=RequestContext(request))

def event_new_pool_post(request, event_id):
	print('\n I see the post! \n ')
	new_pool_form = NewPoolForm(request.POST)
	if new_pool_form.is_valid():
		term = event_form.cleaned_data['term']
		name = event_form.cleaned_data['name']
		num_members = event_form.cleaned_data['number_of_members']
		new_pool = Pool(term=term, name=name)
		new_pool.save()
		tied_event = Event.objects.get(pk=event_id)
		tied_event.pools.add(new_pool)
		tied_event.save()
	event(request, event_id)
