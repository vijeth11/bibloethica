from django.shortcuts import render

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
def some_name(request):

    return render(request, 'some_name.html.html')