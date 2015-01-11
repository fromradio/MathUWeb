import string
import urllib2
import re
from copt.models import Chapter
from home.models import Project

def construct( filename ):
	text = open(filename).read()
	classname = re.search(r'"chaptername".*?>\s*(.*?)\s*</div>',text,re.S).group(1)
	copt = Project.objects.get(title="COPT")
	print copt.chapter_set.all()
	if copt.chapter_set.all().filter(name=classname).exists():
		chapter = copt.chapter_set.all().get(name=classname)
	else:
		chapter = copt.chapter_set.all().create(name=classname)
	intro = re.search(r'"introduction".*?>\s*(.*?)\s*</div>',text,re.S)
	if intro:
		chapter.introduction_set.all().delete()
		chapter.introduction_set.create(content=intro.group(1))
	match_list = re.findall(r'"definition".*?>\s*(.*?)\s*</div>.*?"description".*?>\s*(.*?)\s*</div>',text,re.S)
	chapter.item_set.all().delete()
	for match in match_list:
		chapter.item_set.create(name=match[0],description=match[1])
	chapter.save()