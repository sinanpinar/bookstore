from django.urls import path
from . import views

urlpatterns = [
    path("",views.books,name="books"),
    path("publisher/<slug:slug>",views.publisher,name="publisher"),
    path("writer/<slug:slug>",views.writer,name="writer"),
    path("category/<slug:slug>",views.category,name="category"),
    path("book/<slug:slug>",views.book,name="book"),
]
