from django.shortcuts import render , HttpResponse

def home(req):
    return HttpResponse("this is home page site")