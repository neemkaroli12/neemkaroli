from django.shortcuts import render

# Create your views here.

def home_two(request):
    return render(request,'index.html')

def about_seo(request):
    return render(request,'seo.html')