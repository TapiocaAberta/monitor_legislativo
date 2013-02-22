from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext

def homepage(request):
    return render_to_response('index.html', RequestContext(request))
