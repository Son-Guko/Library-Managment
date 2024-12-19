from django import forms
from .models import *


class CategeoryForm(forms.ModelForm):
    class Meta:
        model = Categeory
        fields = ['name']

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'})
        }

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'author_name': forms.TextInput(attrs={'class': 'form-control'}),
            'book_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'author_photo': forms.FileInput(attrs={'class': 'form-control'}),
            'pages': forms.NumberInput(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control'}),
            'rental_price_day': forms.NumberInput(attrs={'class': 'form-control', 'id': 'rentprice'}),
            'rent_period': forms.TextInput(attrs={'class': 'form-control', 'id': 'rentperiod'}),
            'total_rented':forms.NumberInput(attrs={'class': 'form-control', 'id': 'total'}),
            'statues': forms.Select(attrs={'class': 'form-control'}),
            'categeory': forms.Select(attrs={'class': 'form-control'}),
            
        }
