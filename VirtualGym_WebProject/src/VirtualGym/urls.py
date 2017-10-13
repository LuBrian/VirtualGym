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

from . import home
from users import views as us
from exercise import views as ex
from forum import views as fo

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', home.index, name='index'),

    url(r'^logout/$', us.logOut, name='logout'),
    url(r'^signIn/$',us.signIn,name="signIn"),
    url(r'^signUp/$',us.signUp,name = "signUp"),
    url(r'^createExercise/$',ex.CreateExe,name = "createExercise"),
    url(r'^viewProfile/$',ex.Profile,name = "viewProfile"),
    url(r'^(?P<id>\d+)/$',ex.Exercise_detail,name = "detail"),
    url(r'^QA/$',fo.CreateQuestion,name = "QA"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
