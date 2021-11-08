"""finalproduct URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from testapp import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view),
    url(r'^all-images/$', views.images_view),
    url(r'^all-pdfs/$', views.pdfs_view),
	url(r'^search/$',views.search_view),
	url(r'^(?P<id>\d+)/share/$',views.mail_view),
	url(r'^(?P<id>\d+)/get-users-post/$', views.get_particular_view),
	url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view,name='post_detail'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
