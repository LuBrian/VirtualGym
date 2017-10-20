from django.http import HttpResponse
from django.template import loader
from django.shortcuts import get_object_or_404, render


def index(request):
    """
    render for index.html, set page tite as home
    """
    return render(
        request,
        'index.html',
        {'page_title':"Home"},
    )
