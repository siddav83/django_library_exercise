from django.shortcuts import render
from django.http import HttpResponse
from . models import Book
# Create your views here.

def home(req):
    context = [
    { 'id': 1, 'title': 'Life, the Universe and Everything', 'author': 'Douglas Adams'},
    { 'id': 2, 'title': 'The Meaning of Liff', 'author': 'Douglas Adams'},
    { 'id': 3, 'title': 'The No. 1 Ladies\' Detective Agency', 'author': 'Alexander McCall Smith'}
]
    # context = { 'books': Book.objects.all() }
    
    return render(req, 'home.html', {"books": context})

def about(req):
    return HttpResponse("<h1>Hello! in ABOUT<h1>")

def show(req, id):
    return HttpResponse(f'<h3>Dog number {id}!</h3>')
