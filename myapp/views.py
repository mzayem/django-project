from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'index.html')


def greeting(request):
    return HttpResponse("<h1 style='color:blue'>Hello, world. You're at the About page.</h1> <p>blah blah blah</p>")

def test(request):
    return HttpResponse("Hello, test. You're at the Test page.")

