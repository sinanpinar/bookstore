from django.shortcuts import render
from .models import Book,Category,Publisher,Writer

# Create your views here.

def books(request):
    context={
        "books":Book.objects.all()[::-1],
        "categories":Category.objects.all(),
    }
    return render(request,"books/books.html",context)

def writer(request,slug):
    context={
        "books":Book.objects.filter(writer__slug=slug)[::-1],
        "categories":Category.objects.all(),
    }
    return render(request,"books/books.html",context)

def publisher(request,slug):
    context={
        "books":Book.objects.filter(publisher__slug=slug)[::-1],
        "categories":Category.objects.all(),
    }
    return render(request,"books/books.html",context)

def category(request,slug):
    context={
        "books":Book.objects.filter(categories__slug=slug)[::-1],
        "categories":Category.objects.all(),
    }
    return render(request,"books/books.html",context)

def book(request,slug):
    context={
        "book":Book.objects.get(slug=slug),
        "categories":Category.objects.all(),
    }
    return render(request,"books/detail.html",context)
