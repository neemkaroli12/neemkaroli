from django.shortcuts import render
from .forms import ContactForm 

def contact(request):
    form = ContactForm()
    return render(request, 'my_app/contact.html', {'myData': form})


def home_two(request):
    return render(request,'my_app/index.html')

def about_seo(request):
    return render(request,'my_app/seo.html')

def web(request):
    return render(request,'my_app/web.html')

def media(request):
    return render(request,'my_app/smm.html')


def content(request):
    return render(request,'my_app/content.html')

def pay(request):
    return render(request,'my_app/ppc.html')

def gmb(request):
    return render(request,'my_app/gmb.html')