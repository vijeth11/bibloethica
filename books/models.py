from django.db import models

# Create your models here.
class Books (models.Model):
    isbn = models.CharField(max_length=20)
    title=models.CharField(max_length=30)
    author=models.CharField(max_length=20)
    year=models.IntegerField()

    def __str__(self):
        return "isbn= "+self.isbn+" title= "+self.title+" author= "+self.author+" year= "+str(self.year)

class Users (models.Model):
    username = models.CharField(max_length=20)
    useremail=models.CharField(max_length=20)
    password=models.CharField(max_length=20)

    def __str__(self):
        return "username= "+self.username+" email= "+self.useremail