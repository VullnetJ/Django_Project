from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

# Create your views here.


def contact(request):
    if request.method == 'POST':
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']


    send_mail(
        'Subject here',
        'Here is the message.',
        'v.jata24@gmail.com',
        ['v.jata24@gmail.com'],
        fail_silently=False,
    )

