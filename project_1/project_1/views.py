from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>this is home page</h1>")

def contact(request):
    return HttpResponse("<h1>this is contact page</h1>")