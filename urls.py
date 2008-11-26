from django.conf.urls.defaults import *

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    # (r'^codereviewtool/', include('codereviewtool.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # /
    # /reviews
    # /review/{review.id}
    # /review/{review.id}/files
    # /review/{review.id}/file/{reviewFile.name}
    # /user/{username}
    # /user/{username}/reviews

    # Uncomment the next line to enable the admin:
    (r'^admin/(.*)', admin.site.root),
)
