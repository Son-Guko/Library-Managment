from django.db import models

# Create your models here.

class Categeory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Book(models.Model):
    book_statues = [
        ('Available', 'Available'),
        ('Rented', 'Rented'),
        ('Sold', 'Sold')
    ]

    title = models.CharField(max_length=200, )
    author_name = models.CharField(max_length=200, )
    book_photo = models.ImageField(upload_to='photos', null=True, blank=True)
    author_photo = models.ImageField(upload_to='photos', null=True, blank=True)
    pages = models.IntegerField(null=True, blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True) 
    rental_price_day = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True) 
    rent_period = models.IntegerField(null=True, blank=True)
    total_rented = models.DecimalField(max_digits=10, decimal_places=3, null=True, blank=True)
    active = models.BooleanField(default=True)
    statues = models.CharField(max_length=50, choices=book_statues)
    categeory = models.ForeignKey(Categeory, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title