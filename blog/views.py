from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import loader
from django.http import request
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse

def index(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('blog/index.html', context_dict, context)


def about(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('blog/about.html', context_dict, context)

def shop(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('blog/shop.html', context_dict, context)

def login(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('blog/login.html', context_dict, context)

def register(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('blog/register.html', context_dict, context)


def ladies(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('blog/ladies.html', context_dict, context)

def gents(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('blog/gents.html', context_dict, context)

def contacts(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('blog/contacts.html', context_dict, context)

def gallery(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('blog/gallery.html', context_dict, context)