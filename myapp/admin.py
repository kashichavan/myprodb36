from django.contrib import admin
from django.contrib.admin.decorators import register
from .models import Author,Book
# Register your models here.

@register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display=['name','age']

@register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display=['book_name','book_price','author']


