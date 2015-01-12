from django.shortcuts import get_object_or_404, render
from copt.models import Chapter
import os.path

def index(request):
	chapters = Chapter.objects.all()
	return render(request,'copt/index.html',{'chapters':chapters})

def chapter(request,chapter_name):
	chap = get_object_or_404(Chapter,name=chapter_name)
	item_list = chap.item_set.all()
	introduction = chap.introduction_set.all()
	chap_name = 'copt/templates/copt/'+chapter_name+'.html'
	if(os.path.exists(chap_name)):
		chap_name='copt/'+chapter_name+'.html'
		return render(request,chap_name,{'chapter':chap})
	else:
		return render(request,'copt/chapter.html',{'intro_list':introduction,'item_list':item_list,'chapter':chap})
def test():
	chapter_name = 'VectorBase'
	chap_name = 'copt/templates/copt/'+chapter_name+'.html'
	print chap_name
	print os.path.exists(chap_name)