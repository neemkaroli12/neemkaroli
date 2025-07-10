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
        path('media/',views.media,name='media')
]
