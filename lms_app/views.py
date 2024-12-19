from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import BookForm, CategeoryForm
import os

# Create your views here.

def index(request):
    if request.method == 'POST':
        add_book = BookForm(request.POST, request.FILES)
        add_categeory = CategeoryForm(request.POST)
        if add_book.is_valid():
            add_book.save()
        if add_categeory.is_valid():
            add_categeory.save()
            
    context = {
        'books':Book.objects.all(),
        'categeories':Categeory.objects.all(),
        'form': BookForm(),
        'categeoryform': CategeoryForm(),
        'allbooks':Book.objects.filter(active= True).count(),
        'sold':Book.objects.filter(statues= 'Sold').count(),
        'available':Book.objects.filter(statues= 'Available').count(),
        'rented':Book.objects.filter(statues= 'Rented').count(),
    }
    

    return render(request,'pages/index.html', context)

def books(request):
    title = None
    search = Book.objects.all()
    if 'search_name' in request.GET:
        title = request.GET('search_name')
        if title:
            search = search.filter(title__icontains = title)

    context = {
        'books':search,
        'categeories':Categeory.objects.all(),
    }
    return render(request, 'pages/books.html', context)

def update(request, id):
    book_id = Book.objects.get(id= id)
    if request.method == 'POST':
        book_save = BookForm(request.POST, request.FILES, instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect('/')
    else:
        book_save = BookForm(instance=book_id)

    context  ={
        'form': book_save
    }
    return render(request, 'pages/update.html', context)

def delete(request, id):
    book_delete = get_object_or_404(Book, id= id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect('/')
    return render(request, 'pages/delete.html')

