from django.conf.urls import patterns, include, url

# Moving wow specific context processors here
from django.conf import global_settings, settings
settings.TEMPLATE_CONTEXT_PROCESSORS = global_settings.TEMPLATE_CONTEXT_PROCESSORS + (
    "ffxiv.context_processors.characters",
)

 
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('ffxiv.views',
    # Examples:
    # url(r'^$', 'newmjidemo.views.home', name='home'),
    # url(r'^newmjidemo/', include('newmjidemo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    #
    # \/
    # (________>

    url(r'^$', 'index', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^archive/', 'archive', name='archive'),
    url(r'^gallery/', 'gallery', name='gallery'),
    url(r'^new_article/', 'new_article_page', name='new_article'),
    url(r'^save_article/', 'save_article', name='save_article'),
    url(r'^new_screenshot/', 'new_screenshot_page', name='new_screenshot'),
    url(r'^save_screenshot/', 'save_screenshot', name='save_screenshot'),
    url(r'^logout/', 'logout_view', name='logout'),
    url(r'^login/', 'login_view', name='login'),
)	

