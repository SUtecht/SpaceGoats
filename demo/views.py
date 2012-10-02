from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from demo.models import *
from django.http import Http404
from django.utils import timezone
from dateutils import relativedelta
import datetime
from django.core import serializers
import battlenet
from battlenet import Realm, Guild
from django.shortcuts import redirect
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth import login
from django.contrib.auth.hashers import make_password
from django.contrib.auth.decorators import login_required

from demo.utils import update_character

# old imports not being used anymore, probably need to be deleted
# import glob
# import Image
# from django.contrib.staticfiles.urls import staticfiles_urlpatterns
# from django.core.urlresolvers import reverse


def index(request):
    approved_articles = Article.objects.all().filter(approved = 'Y')
    latest_articles = approved_articles.order_by('-id') #[:3] # <-- temporarily set to everything
    return render_to_response('demo/home.html', {'articles': latest_articles },
                                                context_instance=RequestContext(request))

def eventsJson(request):
    month_start = datetime.datetime(timezone.now().year, timezone.now().month, 1, 0)
    next_month = month_start+relativedelta(months=+1)
    month_end = next_month+relativedelta(seconds=-1)
    
    data = serializers.serialize("json", Event.objects.all())
    return HttpResponse(data, content_type="text/plain")

def event(request, event_id):
    if request.method == 'POST':
        print('\n I see the post! \n ')
        at_form = AttendForm( request.user, request.POST)
        if at_form.is_valid():
            char = at_form.cleaned_data['char']
            event = Event.objects.get(pk=event_id)
            role = at_form.cleaned_data['role']
            attendee = Event_Attendee(event=event, character= Character.objects.get(pk = char), role=role)
            try:
                attendee.save()
            except Exception as e:
                pass
            
    event = Event.objects.get(pk=event_id)
    at_form = None
    if request.user.is_authenticated():
        at_form = AttendForm(request.user)
    attendees = Event_Attendee.objects.filter(event=event).order_by('role')
 
    '''for c in attendees:
        c.bnet = battlenet.Character(battlenet.UNITED_STATES, c.server, c.name)
        print(c.bnet)
    if len(attendees) > 0:
        print(attendees[0].bnet)'''
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
    gows =  Goat_of_the_Week.objects.all().order_by('-id')
    return render_to_response('demo/archive.html', {'articles':articles,
                                                    'gows':gows},
                                                context_instance=RequestContext(request))

def article(request,article_id):
    article = Article.objects.get(pk=article_id)
    return render_to_response('demo/article.html', {'article':article},
                                                context_instance=RequestContext(request))

@login_required  
def new_article_page(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
    else:
        article_form = ArticleForm()
    return render_to_response('demo/new_article.html', {'article_form':article_form},
                                                context_instance=RequestContext(request))

@login_required                                             
def save_article(request):
    if request.method == 'POST':
        # print 'I see the post!'
        article_form = ArticleForm(request.POST, request.FILES)
        if article_form.is_valid():
            # print 'it is valid!'
            title = article_form.cleaned_data['title']
            text = article_form.cleaned_data['text']
            img = article_form.cleaned_data['img']
            new_article = Article(title=title, text=text, img=img, 
                                  author= request.user, approved=False)
            new_article.save()

            return redirect('home')
    return new_article_page(request)

@login_required  
def new_g_o_w(request):
    if request.method == 'POST':
        g_o_w_form = Goat_of_the_Week_Form(request.POST)
    else:
        g_o_w_form = Goat_of_the_Week_Form()
    return render_to_response('demo/g_of_week_new.html', {'g_o_w_form':g_o_w_form},
                                                context_instance=RequestContext(request))
    
def save_g_o_w(request):
    if request.method == 'POST':
        # print 'I see the post!'
        g_o_w_form = Goat_of_the_Week_Form(request.POST, request.FILES)
        if g_o_w_form.is_valid():
            # print 'it is valid!'
            name = g_o_w_form.cleaned_data['name']
            img = g_o_w_form.cleaned_data['img']
            desc = g_o_w_form.cleaned_data['desc']
            new_goat_of_week = Goat_of_the_Week(name=name,  img=img, 
                                  desc = desc)
            new_goat_of_week .save()

            return redirect('home')
    return new_g_o_w(request)

def gow(request,gow_id):
    my_gow = Goat_of_the_Week.objects.get(pk=gow_id)
    return render_to_response('demo/gow.html', {'my_gow':my_gow},
                                                context_instance=RequestContext(request))

def register_failed(request, error_message):
        if request.method == 'POST':
            new_user_form = NewUserForm(request.POST)
        return render_to_response('demo/register.html',{'new_user_form':new_user_form, 'error_message':error_message } ,
                                                context_instance=RequestContext(request))
                                                
def register(request ):                                               
        new_user_form = NewUserForm()
        return render_to_response('demo/register.html',{'new_user_form':new_user_form } ,
                                                context_instance=RequestContext(request)) 
                                                
def register_view(request):
    if request.method == 'POST':
        new_user_form = NewUserForm(request.POST)
        if new_user_form.is_valid():
            username = request.POST['username']
            for u in User.objects.all() :
                if username == u.username:
                    error_message = "Username is taken."
                    return register_failed(request, error_message)
            password = make_password(request.POST['password'])
            email = request.POST['email']
            character = request.POST['character']
            server = request.POST['server']
            try:
                c = battlenet.Character(battlenet.UNITED_STATES, server, character)
            except Exception as e:
                    error_message = "This character does not exist on this server."
                    return register_failed(request, error_message)
            user = User(username=username, password=password, email=email)
            user.save()
            login_user = authenticate(username=username, password=request.POST['password'])
            login(request, login_user)
            character = Character(name=character, server=server, player=user, class_name='', level=0, ilvl=0)
            character.save()
            update_character(character)
            player = Player(user=user, main=character)
            player.save()
            return redirect('home')
        else:
            error_message = "There was a problem with your application."
            return register_failed(request, error_message)
    else:
        return redirect('home')

def logout_view(request):
    logout(request)
    return redirect('home')

def login_view(request):
    error_message = None

    if request.method == 'POST':
        #create new user
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # return an error message
            error_message = "Login or password was invalid!"


    #display page for logging in
    login_form = LoginForm()
   
    return render_to_response('demo/login.html',
            dict(login_form=login_form, 
                 error_message=error_message),
            context_instance=RequestContext(request))

