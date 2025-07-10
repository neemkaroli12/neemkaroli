from django.shortcuts import render

# Create your views here.

def home_two(request):
    return render(request,'my_app/index.html')

def about_seo(request):
    return render(request,'my_app/seo.html')

def web(request):
    return render(request,'my_app/web.html')

def media(request):
    return render(request,'my_app/smm.html')

def contact(request):
    return render(request,'my_app/contact.html')