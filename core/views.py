from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Project, Skill, ContactMessage

def home(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            ContactMessage.objects.create(name=name, email=email, message=message)
            messages.success(request, 'TRANSMISSION_SUCCESS: Uplink data securely logged.')
            return redirect('home')
        else:
            messages.error(request, 'ERROR: Incomplete data payload detected.')

    projects = Project.objects.all()
    skills = Skill.objects.all()

    context = {
        'projects': projects,
        'skills': skills,
    }
    return render(request, 'core/index.html', context)
