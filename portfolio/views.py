from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

def home(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message_text = request.POST.get('message')

        Contact.objects.create(
            name=name,
            email=email,
            message=message_text
        )

        messages.success(request, "Your message has been sent successfully!")
        return redirect('/#contact')

    return render(request, 'index.html')

from django.contrib.auth.models import User
from django.http import HttpResponse

def create_admin(request):
    if not User.objects.filter(username="Hari1483").exists():
        User.objects.create_superuser(
            username="Hari1483",
            email="ahari1483@gmail.com",
            password="Akruachu1*"
        )
        return HttpResponse("Superuser created")

    return HttpResponse("Superuser already exists")