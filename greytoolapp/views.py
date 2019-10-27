from django.shortcuts import render
from greytoolapp.models import Project
from django.http import HttpResponseRedirect

# Create your views here.
def index(request):
    projects = Project.objects.all()
    context = { 'projects': projects }
    return render(request, "project_index.html", context)

def project(request, pk):
    project = Project.objects.get(pk=pk)
    context = { 'project': project }
    return render(request, 'project_detail.html', context)

def addProject(request):
    return render(request, 'project_add.html')

def addProjectButton(request):
    if request.method=='POST':
        post = request.POST
        Project.objects.create(
            title=post.get("titulo"), 
            description=post.get("descricao"),
            technology=post.get("tecnologia"),
            image=post.get("foto_url")
        )
        return HttpResponseRedirect("/projects")

def rmProjectButton(request, pk):
    p = Project.objects.get(pk=pk)
    p.delete()
    return HttpResponseRedirect("/projects")
