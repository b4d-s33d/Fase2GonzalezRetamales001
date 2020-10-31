from django.shortcuts import render
from .models import Libro, Autor, Genero

# Create your views here.
def index(request):
    num_books = Libro.objects.all().count()
    num_authors = Autor.objects.all().count()
    return render(
        request,
        'index.html',
        context={'num_books':num_books, 'num_authors':num_authors,}
    )

def ranking(request):  
    books = Libro.objects.all()
    return render(request, 'ranking.html', context={'books':books,})  

def login(request):  
    return render(request, 'login.html')  

def register(request):  
    return render(request, 'register.html')          