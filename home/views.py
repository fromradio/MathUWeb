from django.shortcuts import render
from home.models import Project

# Create your views here.
def index(request):
	project_list = Project.objects.all()
	context = {'project_list':project_list}
	return render(request,'home/index.html',context)