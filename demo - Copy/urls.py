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
	url(r'^pool_view/(?P<pool_id>\d+)', 'pool_view'),
	url(r'^pool_member/(?P<voter_id>\d+)', 'pool_member'),
	url(r'^event/(?P<event_id>\d+)', 'event'),
	url(r'^event/(?P<event_id>\d+)/np', 'event_new_pool_post'),
)	

