from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.http import HttpResponse

from polls.models import Poll


def index(request):
	latest_question_list = Poll.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list}
	return render(request,'polls/index.html',context)
	
def detail(request, question_id):
	question = get_object_or_404(Poll,pk=question_id)
	return render(request,'polls/detail.html',{'question':question})

def results(request, question_id):
	question = get_object_or_404(Poll,pk=question_id)
	return render(request,'polls/results.html',{'question':question})

def vote(request, question_id):
	question = get_object_or_404(Poll,pk=question_id)
	return render(request,'polls/vote.html',{'question':question})