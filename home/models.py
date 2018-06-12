from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=200, blank=False)
    email = models.EmailField(max_length=200, blank=False)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=254, default='')
    description = models.TextField()
    author = models.ForeignKey(Author, related_name="books", null=False)

    def __str__(self):
        return self.name
        
