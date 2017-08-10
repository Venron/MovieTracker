from django.shortcuts import redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth



def index(request):
    return redirect("/tracker/")