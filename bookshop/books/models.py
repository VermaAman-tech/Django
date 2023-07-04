from django.db import models
# Create your models here.

class Contact(models.Model):
    firstname=models.CharField(max_length=20)
    lastname=models.CharField(max_length=20)
    phonenumber=models.PositiveIntegerField()
    email=models.EmailField()
    comments=models.TextField()
    
    def __str__(self):
        return self.firstname+" "+self.lastname
 
    
    
class AddBook(models.Model):
    author=models.CharField(max_length=100)
    title=models.CharField(max_length=100)
    price=models.PositiveIntegerField()
    description=models.TextField()
    book_objects=models.Manager()
    
    def __str__(self):
        return self.author+" "+self.title
    
    

 
    
 