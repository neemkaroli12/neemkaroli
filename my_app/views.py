from django.shortcuts import render, get_object_or_404
from .forms import ContactForm
from .models import JobPost ,JobPostForm

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

def about_us(request):
    return render(request,'my_app/about.html')

def career(request):
    return render(request,'my_app/career.html')


def career(request):
    selected_types = request.GET.getlist('job_type')
    jobs = JobPost.objects.all().order_by('-posted_on')

    if selected_types:
        jobs = jobs.filter(job_type__in=selected_types)

    context = {
        'jobs': jobs,
        'selected_types': selected_types,
    }
    return render(request, 'my_app/career.html', context)

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



