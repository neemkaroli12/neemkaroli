from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

app_name='my_app'

urlpatterns = [
        path('',views.home_two ,name='home_two'),
        path('seo/',views.about_seo ,name='about'),
        path('web/',views.web, name='web'),
        path('media/',views.media,name='media'),
        path('contact/',views.contact,name='contact'),
        path('content/',views.content,name='content'),
        path('pay/',views.pay,name='pay'),
        path('gmb/',views.gmb,name='gmb'),
        path('about/',views.about_us,name='about_us'),
        path('career/',views.career,name='career'),
        path('job/<int:pk>/', views.job_detail, name='job_detail'),
        path('career/add/', views.add_job, name='add_job'),
        path('delete/<int:job_id>/', views.delete_job, name='delete_job'),
        path('creative/',views.creative,name="creative"),
        path('b2b/',views.b2b,name="b2b"),

]
