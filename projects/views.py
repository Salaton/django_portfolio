from django.shortcuts import render
from projects.models import Project
# Create your views here.

# Create a function that renders a html page and select all objects from the projects table


def project_index(request):
    # performing a query to retrieve all objects in the Projects table..
    projects = Project.objects.all()
    context = {
        'projects': projects
    }

    return render(request, 'project_index.html', context)


def project_detail(request, pk):
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }

    return render(request, 'project_detail.html', context)
