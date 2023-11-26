from django.urls import path
from . import views

urlpatterns = [
    path('', views.front, name='front'),
    path('contact-us-form', views.contact_us, name='contact-us'),
]