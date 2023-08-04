from django.shortcuts import render
from .models import Project, Task
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render


# Create your views here.

def  hello(request, username):
    return HttpResponse("<h2>Hellow %s</h2>" % username)

def  index(request):
    return render(request, 'index.html')

def  about(request):
    return render(request, 'about.html')

def  projects(request):
    
    projects = Project.objects.all()
    #return JsonResponse(projects, safe=False)
    return render(request, 'projects.html', {
        'projects':projects
    })


def  tasks(request):
    #return HttpResponse ("tasks")
    tasks = Task.objects.all()
    return render(request, 'tasks.html', {
        'tasks':tasks
        
    })
