from django.conf.urls import patterns, include, url


 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('demo.views',
    # Examples:
    # url(r'^$', 'newmjidemo.views.home', name='home'),
    # url(r'^newmjidemo/', include('newmjidemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #
    # \/
    # (________>
    url(r'^$', 'index'),
    url(r'^ajax/events.json', 'eventsJson'),
    url(r'^event/(?P<event_id>\d+)', 'event'),
    url(r'^about/', 'about'),
    url(r'^archive/', 'archive'),
    url(r'^article/(?P<article_id>\d+)', 'article'),

    # url(r'^mockup/', 'mockup'),
    url(r'^new_article/', 'new_article_page'),
    url(r'^save_article/', 'save_article'),
)	

