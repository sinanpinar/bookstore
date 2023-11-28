from typing import Any
from django.db import models
from django.utils.text import slugify

class Writer(models.Model):
    name=models.CharField(max_length=50)
    surname=models.CharField(max_length=50)
    slug=models.SlugField(null=True,blank=True, unique=True,db_index=True, editable=False)

    def __str__(self):
        return self.name+" "+self.surname
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name+" "+self.surname)
        super().save(*args,**kwargs)
        

class Publisher(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(null=True,blank=True, unique=True,db_index=True,editable=False)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)

class Category(models.Model):
    name=models.CharField(max_length=50)
    slug=models.SlugField(null=True,blank=True, unique=True,db_index=True,editable=False)

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)


class Book(models.Model):
    name=models.CharField(max_length=50)
    description=models.TextField()
    page=models.IntegerField()
    writer=models.ForeignKey(Writer,on_delete=models.CASCADE)
    publisher=models.ForeignKey(Publisher,on_delete=models.CASCADE)
    categories=models.ManyToManyField(Category)
    createDate=models.DateField()
    slug=models.SlugField(null=True,blank=True, unique=True ,db_index=True ,editable=False)
    image=models.ImageField(upload_to="books/image")
    pdf=models.FileField(default="", upload_to="books/pdf")

    def __str__(self):
        return self.name
    
    def save(self,*args,**kwargs):
        self.slug=slugify(self.name)
        super().save(*args,**kwargs)





