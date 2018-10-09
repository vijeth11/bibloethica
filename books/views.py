import ast
import json
from django.http import HttpResponse
from django.shortcuts import render
from .models import Books,Users
from django.db.models import Q
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
            responseObject={}
            user=Users.objects.get(username=data['username'],password=data['password'])
            data=(user.get()).split(";")
            for d in data:
                key,value=d.split("=")
                responseObject[key]=value
            responseObject["status"]="found"
            responseObject["error"]="null"
        except Users.DoesNotExist:
            return HttpResponse(json.dumps({'status':'error','error':'user does not exist'}), content_type="application/json")
        except KeyError:
            return HttpResponse(json.dumps({'status':'error','error':'key value error '}), content_type="application/json")
    return HttpResponse(json.dumps(responseObject), content_type="application/json")

@csrf_exempt
def getbook(request):
    responsedata={}
    if(request.method=='POST'):
        try:
            data=ast.literal_eval(request.read().decode("utf-8"))
            book=Books.objects.get(isbn=data['isbn'])
            data=(book.get()).split(";")
            responsedata={}
            for d in data:
                key,value=d.split("=")
                responsedata[key]=value
            responsedata["status"]="found"
            responsedata["error"]="null"
        except Books.DoesNotExist:
            return HttpResponse(json.dumps({'status':'error','error':'book not found'}), content_type="application/json")
    return HttpResponse(json.dumps(responsedata), content_type="application/json")

@csrf_exempt
def register(request):
    if(request.method=='POST'):
        try:
            data=ast.literal_eval(request.read().decode("utf-8"))
            user=Users.objects.get(Q(username=data['username'])|Q(useremail=data['useremail']))

        except Users.DoesNotExist:
            try:
                userinstance = Users.objects.create(username=data['username'], useremail=data['useremail'],
                                                    password=data['password'])
            except:
                return HttpResponse(json.dumps({'status':'error','error':'user not registered'}), content_type="application/json")
            return HttpResponse(json.dumps({'status':'success','error':'null'}), content_type="application/json")
    return HttpResponse(json.dumps({'status': 'error', 'error': 'user already exists'}), content_type="application/json")


def getfirstsetbooks(request):
    if(request.method=='GET'):
        try:
            response=[]
            print("i am here")
            books=Books.objects.all()[:10]
            print(Books.objects.all()[:10])
            for book in books:
                data=(book.get()).split(";")
                dict={}
                for d in data:
                    key,value=d.split("=")
                    dict[key]=value
                response.append(dict)
        except Books.DoesNotExist:
            return HttpResponse(json.dumps({'status': 'error', 'error': 'books not found'}), content_type="application/json")

    return HttpResponse(json.dumps(response), content_type="application/json")