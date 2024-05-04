from django.db import models

# Create your models here.

class Author(models.Model):
    name=models.CharField(max_length=25)
    age=models.IntegerField()
    
    def __str__(self):
        return self.name

class Book(models.Model):
    book_name=models.CharField(max_length=25)
    book_price=models.FloatField()
    author=models.ForeignKey(Author,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.book_name

