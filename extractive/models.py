from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length=120)
    abstract = models.CharField(max_length=250)
    content = models.TextField()
    image = models.ImageField(upload_to='pics/')
    date = models.DateField()
    typee = models.CharField(max_length=20)
    author = models.CharField(max_length=60)
    aboutauthor = models.CharField(max_length=400)
    authorimage = models.ImageField(upload_to='pics') #,blank=True
    links = models.URLField()

class Contact(models.Model):
    fname = models.CharField(max_length=120)
    lname = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=250)
    message = models.TextField()

