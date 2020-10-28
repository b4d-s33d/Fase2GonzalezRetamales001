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