from django.conf.urls import url
from django.contrib import admin
from app.views import *
from django.conf import settings
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import include

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', signup_user.as_view()),
    url(r'^login/$',login.as_view()),
    url(r'^activate/$',activate.as_view()),
    url(r'^api-auth/', include('rest_framework.urls')),
    url(r'^forgot_password/$',forgot_password.as_view()),
    url(r'^reset_password/$',reset_password.as_view()),
    url(r'^edit_user/$',edit_user.as_view()),
    url(r'^delete_user/$',delete_user.as_view()),
    url(r'^display/$',display.as_view()),

    


    
    
    
    
    
]