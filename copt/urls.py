from django.conf.urls import url
from copt import views

urlpatterns = [
	# ex: /copt/
	url(r'^$',views.index,name='index'),
	# ex: /copt/chapter/
	url(r'^(?P<chapter_name>[A-z]+)/$',views.chapter,name='chapter'),
]