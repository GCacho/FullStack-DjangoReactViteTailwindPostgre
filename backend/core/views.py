# from django.http import HttpResponse
from django.shortcuts import render

def home_view(request):
    value = "Hello World! :)"
    return render(request,'main.html',{'hello_key':value})