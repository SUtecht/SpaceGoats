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
import battlenet
import glob
import Image
from battlenet import Realm, Guild
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


def eventsJson(request):
    month_start = datetime.datetime(timezone.now().year, timezone.now().month, 1, 0)
    next_month = month_start+relativedelta(months=+1)
    month_end = next_month+relativedelta(seconds=-1)
    
    data = serializers.serialize("json", Event.objects.all())
    return HttpResponse(data, content_type="text/plain")

def index(request):

    
    
        
    if request.method == 'POST':
        print('\n I see the post! \n ')
        event_form = EventForm(request.POST)
        if event_form.is_valid():
            print('\n Valid Event! \n')
            name = event_form.cleaned_data['name']
            begin = event_form.cleaned_data['begin_date']
        
            new_event = Event(name=name, begin=begin)
            new_event.save()
            print('\n Event created!\n')
            event_form = EventForm()
        else:
            print(event_form.errors)
    else:		
        event_form = EventForm()
    latest_articles = Article.objects.all().order_by('-id')[:5]
    print(latest_articles)
    return render_to_response('demo/index.html', {'event_form':event_form,
                                                    'timezone':timezone,
                                                    'latest_articles':latest_articles},
                                                    context_instance=RequestContext(request))
    

                                                        

                                                    
def event(request, event_id):
    if request.method == 'POST':
        print('\n I see the post! \n ')
        at_form = AttendForm(request.POST)
        if at_form.is_valid():
            char = at_form.cleaned_data['char']
            event = Event.objects.get(pk=event_id)
            print(char)
            event.attendees.add(char)
            event.save()

    event = Event.objects.get(pk=event_id)
    at_form = AttendForm()
    attendees = event.attendees.all()
 
    for c in attendees:
        c.bnet = battlenet.Character(battlenet.UNITED_STATES, c.server, c.name)
        print(c.bnet)
    if len(attendees) > 0:
        print(attendees[0].bnet)
    return render_to_response('demo/events.html', {'event':event,
                                                'at_form':at_form,
                                                'attendees':attendees,
                                                'timeszone':timezone},
                                                context_instance=RequestContext(request))


def about(request):
    guild = Guild(battlenet.UNITED_STATES, 'Auchindoun', 'Space Goats CoastToCoast')
    return render_to_response('demo/about.html', {'guild':guild},
                                                context_instance=RequestContext(request))
                                                
def archive(request):
    approved_articles = Article.objects.all().filter(approved = 'Y')
    articles = approved_articles.order_by('-id')
    return render_to_response('demo/archive.html', {'articles':articles},
                                                context_instance=RequestContext(request))
                                                
def article(request,article_id):
    article = Article.objects.get(pk=article_id)
    return render_to_response('demo/article.html', {'article':article},
                                                context_instance=RequestContext(request))



def mockup(request):
    approved_articles = Article.objects.all().filter(approved = 'Y')
    latest_articles = approved_articles.order_by('-id') #[:3] # <-- temporarily set to everything
    all_upcoming_events = Event.objects.all().filter(begin__gte = datetime.date.today())
    soon_events = all_upcoming_events.order_by('begin')[:4]
    return render_to_response('demo/home.html', {'articles': latest_articles,
                                                 'e0':soon_events[0],
                                                 'upcoming_events':soon_events},
                                                context_instance=RequestContext(request))

def new_article_page(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
    else:
        article_form = ArticleForm()
    return render_to_response('demo/new_article.html', {'article_form':article_form},
                                                context_instance=RequestContext(request))
def save_article(request):
    if request.method == 'POST':
        # print 'I see the post!'
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            # print 'it is valid!'
            title = article_form.cleaned_data['title']
            text = article_form.cleaned_data['text']
            img = article_form.cleaned_data['img']
            author = article_form.cleaned_data['author']
            new_article = Article(title=title, text=text, img=img, 
                                  author=author, approved = 'N')
            new_article.save()

            # im = Image.open(new_article.img.url)
            # im.thumbnail((128, 128), Image.ANTIALIAS)
            # print 
            # im.save( settings.STATIC_ROOT + "\\thumbs\T_" + new_article.img.url[8:200])
            #new_article.thumb = temp/T_
            #new_article.save()

            # TODO: Make this use the reverse() thingy
            return redirect('/demo/mockup/')
    return new_article_page(request)
