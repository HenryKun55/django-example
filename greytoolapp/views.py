from django.shortcuts import render
from greytoolapp.models import Project

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = { 'projects': projects }
    return render(request, "project_index.html", context)

def project(request, pk):
    project = Project.objects.get(pk=pk)
    context = { 'project': project }
    return render(request, 'project_detail.html', context)
