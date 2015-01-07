from django.conf.urls import include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'MathUWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^',include('index.urls',namespace="mathu")),
    url(r'^polls/', include('polls.urls',namespace="polls")),
    url(r'^admin/', include(admin.site.urls)),
]
