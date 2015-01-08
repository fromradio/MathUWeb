from django.conf.urls import include, url
from django.contrib import admin
from home import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'MathUWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    # url(r'^',include('index.urls',namespace="mathu")),
    url(r'^$','home.views.index'),
    url(r'^polls/', include('polls.urls',namespace="polls")),
    url(r'^copt/',include('copt.urls',namespace="copt")),
    url(r'^admin/', include(admin.site.urls)),
]
