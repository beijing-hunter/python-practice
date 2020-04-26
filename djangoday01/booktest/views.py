from django.shortcuts import render
from django.http import HttpResponse
from booktest.dao import *
# Create your views here.

def index(request):
    return HttpResponse("<h1>hello world</h1>")

def indexTemplate(request):
    datas={}
    datas["info"]="hello world"
    return render(request,"booktest/index.html",datas)

def findBanks(request):
    datas={}
    datas["info"]=BankDao.findAll()
    return render(request, "booktest/banklist.html", datas)