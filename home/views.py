from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext


def home(request):
    return render_to_response('home/home.html', {}, context_instance=RequestContext(request))


def giris(request):
    return render_to_response('home/giris.html', {}, context_instance=RequestContext(request))


