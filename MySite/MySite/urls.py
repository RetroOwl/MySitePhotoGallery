"""
Definition of urls for MySite.
"""

from datetime import datetime
from django.conf.urls import url
import django.contrib.auth.views

import blog.forms
import blog.views

from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings

from django.conf.urls import include
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', blog.views.home, name='home'),
    url(r'^contact$', blog.views.contact, name='contact'),
    url(r'^about$', blog.views.about, name='about'),
    

    
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    
    url(r'^admin/', admin.site.urls),
    url(r'^register/$', blog.views.RegisterFormView.as_view()),
    url(r'^login/$', blog.views.LoginFormView.as_view()),
    url(r'^logout/$', blog.views.LogoutView.as_view()),
    url(r'^blog/', include('blog.urls', namespace='blog')),
    
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()

