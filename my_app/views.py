from django.shortcuts import render, get_object_or_404, redirect
from .forms import ContactForm
from .models import JobPost ,JobPostForm
from django.core.mail import send_mail
from django.contrib import messages
from django.conf import settings
from django.urls import reverse
from django.core.files.storage import FileSystemStorage
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core.mail import EmailMessage



def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data

            send_mail(
                subject="New Contact Submission",
                message=f"""
Name: {data['name']}
Email: {data['email']}
Phone: {data['phone']}
Designation: {data['designation']}
Message: {data['message']}
""",
                from_email="Neemkaroli Technologies <sales@neemkarolitechnologies.com>",
                recipient_list=['sales@neemkarolitechnologies.com'],
            )

            messages.success(request, "Your message has been sent successfully!")

            return redirect(reverse('my_app:contact'))
    else:
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

def about_us(request):
    return render(request,'my_app/about.html')

def career(request):
    return render(request,'my_app/career.html')


def career(request):
    job_type = request.GET.get('job_type')
    if job_type:
        jobs = JobPost.objects.filter(job_type=job_type)
    else:
        jobs = JobPost.objects.all()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'my_app/job_list.html', {'jobs': jobs})

    return render(request, 'my_app/career.html', {'jobs': jobs})
def job_detail(request, pk):
    job = get_object_or_404(JobPost, pk=pk)
    return render(request, 'my_app/job_detail.html', {'job': job})

def add_job(request):
    if request.method == 'POST':
        form = JobPostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobPostForm()
    
    return render(request, 'my_app/add_job.html', {'form': form})


def delete_job(request, job_id):
    return render(request,'my_app/career.html')

def creative(request):
    return render(request,'my_app/creative.html')

def b2b(request):
    return render(request,'my_app/b2b.html')

def apply_job(request, job_id):
    job = get_object_or_404(JobPost, id=job_id)
    reference = job.reference_number if job.reference_number else "N/A"

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('textarea')
        cv = request.FILES.get('cv')

        subject = f"Ref No: {reference} |{job_id}"
        message = f"Name: {name}\nEmail: {email}\nReference Number: {reference}\nMessage: {message}"

        mail = EmailMessage(
            subject,
            message,
            'sales@neemkarolitechnologies.com',
            ['sales@neemkarolitechnologies.com'],
        )

        if cv:
            mail.attach(cv.name, cv.read(), cv.content_type)

        mail.send()

        if request.headers.get('x-requested-with') == 'XMLHttpRequest':
            return JsonResponse({'status': 'sent'})
        return redirect('my_app:job_detail', pk=job_id)

def web_design(request):
    return render(request,'my_app/web_design.html')

