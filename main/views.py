from django.shortcuts import render
from books.models import Book,Category

# Create your views here.

def index(request):
    context={
        "books":zip(range(5),Book.objects.order_by("createDate")[:5:-1]),
        "categories":Category.objects.all()
    }
    return render(request,"main/index.html",context)
