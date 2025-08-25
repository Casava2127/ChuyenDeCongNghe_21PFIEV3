from django.db import models
from .base import Author

# Many-to-one
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    published = models.DateField()

    def __str__(self):
        return self.title

# Many-to-many
class Store(models.Model):
    name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, through="Stock")

# Extra fields on many-to-many
class Stock(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    store = models.ForeignKey(Store, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

# One-to-one
class AuthorProfile(models.Model):
    author = models.OneToOneField(Author, on_delete=models.CASCADE, related_name="profile")
    bio = models.TextField()
