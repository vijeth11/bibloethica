import ast

from django.http import HttpResponse
from django.shortcuts import render
from .models import Books,Users
# Create your views here.
# from .models import Books
# import csv
# import os
# with open("books/books.csv", 'r') as f:
#   reader = csv.reader(f)
#   for row in reader:
#      print(row)
#      if(str.isnumeric(row[3])):
#         foo_instance = Books.objects.create(isbn=row[0],title=row[1],author=row[2],year=int(row[3]))
#print(os.listdir())
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def login(request):
    if(request.method=='POST'):
        data=ast.literal_eval(request.read().decode("utf-8"))

        try:
            Users.objects.get(username=data['username'],password=data['password'])
        except Users.DoesNotExist:
            return HttpResponse("user not found")
        except KeyError:
            return HttpResponse("key value error ")
    return HttpResponse("hello world")

def getbooks(request,isbn):
    return HttpResponse("yet to be created")