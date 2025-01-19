from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def courses(request):
    return HttpResponse("<h1>this is first app/courses page</h1>")
def about(request):
    return HttpResponse("<h1>this is first app/about page</h1>")
def home(request):
    return HttpResponse("<h1>this is first app/home page</h1>")
