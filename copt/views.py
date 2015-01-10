from django.shortcuts import get_object_or_404, render
from copt.models import Chapter

def index(request):
	chapters = Chapter.objects.all()
	return render(request,'copt/index.html',{'chapters':chapters})

def chapter(request,chapter_name):
	chap = get_object_or_404(Chapter,name=chapter_name)
	item_list = chap.item_set.all()
	introduction = chap.introduction_set.all()
	return render(request,'copt/chapter.html',{'intro_list':introduction,'item_list':item_list,'chapter':chap})