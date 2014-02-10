from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.template import RequestContext
from ffxiv.models import *
import datetime
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate

def index(request):
    # Find last 3 articles
    articles = Article.objects.all().order_by('-id')[:3]
    # Last 5 screenshots
    screenshots = Screenshot.objects.all().order_by('-id')[:5]
    return render_to_response('ffxiv/home.html',
            {'articles':articles, 'screenshots':screenshots},
            context_instance=RequestContext(request))

def archive(request):
    articles = Article.objects.all().order_by('-id')
    return render_to_response('ffxiv/archive.html',
            {'articles':articles},
            context_instance=RequestContext(request))

def gallery(requst):
    screenshots = Screenshot.objects.all().order_by('-id')
    return render_to_response('ffxiv/gallery.html',
            {'screenshots':screenshots},
            context_instance=RequestContext(request))

@login_required  
def new_article_page(request):
    if request.method == 'POST':
        article_form = ArticleForm(request.POST)
    else:
        article_form = ArticleForm()
    return render_to_response('ffxiv/new_article.html', {'article_form':article_form},
                                                context_instance=RequestContext(request))

@login_required                                             
def save_article(request):
    if request.method == 'POST':
        # print 'I see the post!'
        article_form = ArticleForm(request.POST)
        if article_form.is_valid():
            # print 'it is valid!'
            title = article_form.cleaned_data['title']
            text = article_form.cleaned_data['text']
            new_article = Article(title=title, text=text, author= request.user,
                                  creation_date = datetime.date.today())
            new_article.save()

            return redirect('home')
    return new_article_page(request)

@login_required  
def new_screenshot_page(request):
    if request.method == 'POST':
        screenshot_form = ScreenshotForm(request.POST)
    else:
        screenshot_form = ScreenshotForm()
    return render_to_response('ffxiv/new_screenshot.html', {'screenshot_form':screenshot_form},
                                                context_instance=RequestContext(request))

@login_required                                             
def save_screenshot(request):
    if request.method == 'POST':
        # print 'I see the post!'
        screenshot_form = ScreenshotForm(request.POST, request.FILES)
        if screenshot_form.is_valid():
            # print 'it is valid!'
            caption = screenshot_form.cleaned_data['caption']
            img = screenshot_form.cleaned_data['img']
            new_screenshot = Screenshot(caption=caption, user= request.user,
                                  image = img, creation_date = datetime.date.today())
            new_screenshot.save()

            return redirect('home')
    return new_screenshot_page(request)

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
   
    return render_to_response('ffxiv/login.html',
            dict(login_form=login_form, 
                 error_message=error_message),
            context_instance=RequestContext(request))

def logout_view(request):
    logout(request)
    return redirect('home')

