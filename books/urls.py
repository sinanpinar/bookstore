from django.urls import path
from . import views

urlpatterns = [
    path("",views.books,name="books"),
    path("book/<slug:slug>",views.book,name="book"),
    path("writer/<slug:slug>",views.writer,name="writer"),
    path("publisher/<slug:slug>",views.publisher,name="publisher"),
    path("category/<slug:slug>",views.category,name="category"),
    
]
