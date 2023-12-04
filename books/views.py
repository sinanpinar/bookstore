from django.shortcuts import render,redirect
from .models import Book,Category,Publisher,Writer

# Create your views here.
context={
        "books":Book.objects.all()[::-1],
        "categories":Category.objects.all(),
        "writers":Writer.objects.all(),
        "publishers":Publisher.objects.all(),
    }
def books(request):
    if request.method=="GET": 
        books=Book.objects.all()
                
        q=request.GET.get("q")
        if q is not None:
            books = books.filter(name__icontains=q)

        category=request.GET.get("category")
        if category is not None:
            if category != "":
                books = books.filter(categories__slug=category)
            
        publisher=request.GET.get("publisher")
        if publisher is not None:
            if publisher != "":
                books = books.filter(publisher__slug=publisher)

        writer=request.GET.get("writer")
        if writer is not None:
            if writer != "":
                books = books.filter(writer__slug=writer)

        context["books"]=books[::-1]
    return render(request,"books/books.html",context)

def writer(request,slug):
    context["books"]=Book.objects.filter(writer__slug=slug)
    return render(request,"books/books.html",context)

def publisher(request,slug):
    context["books"]=Book.objects.filter(publisher__slug=slug)
    return render(request,"books/books.html",context)

def category(request,slug):
    context["books"]=Book.objects.filter(categories__slug=slug)
    return render(request,"books/books.html",context)

def book(request,slug):
    context["book"]=Book.objects.get(slug=slug)
    return render(request,"books/detail.html",context)
