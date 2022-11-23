from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(req):
    return HttpResponse("<h1>Hello! Here are all the friends who need adopting!<h1>")

def about(req):
    return HttpResponse("<h1>Hello! in ABOUT<h1>")

def show(req, id):
    return HttpResponse(f'<h3>Dog number {id}!</h3>')
