from django.shortcuts import render

def home(request):
    return render(request, "home.html")

def navbar(request):
    return render(request, "navbar.html")