from django.contrib import admin
from .models import Category,Book,Publisher,Writer 

class BookAdmin(admin.ModelAdmin):
    list_display=("name","slug",)
    readonly_fields=("slug",)
    list_filter=("categories",)

# Register your models here.
admin.site.register(Book,BookAdmin)
admin.site.register(Category)
admin.site.register(Publisher)
admin.site.register(Writer)

