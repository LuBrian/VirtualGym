"""VirtualGym URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import logout
from django.conf import settings
from django.conf.urls.static import static

from . import view
from users import views as us
from exercise import views as ex
from forum import views as fo
# from annotations import views as an


urlpatterns = [
    #settings admin page
    url(r'^admin/', admin.site.urls),
    #setting index page
    url(r'^$', view.index, name='index'),
    #setting log out page
    url(r'^logout/$', view.logOut, name='logout'),
    #setting sing in page
    # url(r'^signIn/$',us.signIn,name="signIn"),
    #setting sing up page
    # url(r'^signUp/$',us.signUp,name = "signUp"),
    #setting createExercise page
    url(r'^createExercise/$',ex.CreateExe,name = "createExercise"),
    #setting viewProfile page
    url(r'^viewProfile/$',ex.Profile,name = "viewProfile"),
    #setting myExercise page
    url(r'^myExercise/$',ex.MyExercise,name = "myExercise"),
    #setting exercise detail page according exercise id
    url(r'^(?P<id>\d+)/$',ex.Exercise_detail,name = "detail"),
    #setting QA page
    url(r'^QA/$',fo.CreateQuestion,name = "QA"),
    #setting facebook, google and twitter page
    url(r'^auth/', include('social_django.urls', namespace='social')),
    url(r'^(?P<id>\d+)/edit/$',ex.EditExe,name = "edit"),
    # url(r'^annotations/(?P<vidID>\d+)/$',an.createAnnotation,name = "annotations"),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
