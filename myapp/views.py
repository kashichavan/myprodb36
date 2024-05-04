from django.shortcuts import render
from .models import Author,Book
# Create your views here.
def home(request):
    data=Author.objects.all()
    d={'data':data}
    return render(request,'home.html',context=d)
