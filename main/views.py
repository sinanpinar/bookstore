from django.shortcuts import render
from books.models import Book,Category

# Create your views here.

def index(request):
    context={
        "carousel":zip(range(5),list(Book.objects.all())[:-5:-1]),
        "books":Book.objects.all()[::-1],
        "categories":Category.objects.all()
    }
    return render(request,"main/index.html",context)
