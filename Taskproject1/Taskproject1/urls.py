"""Taskproject1 URL Configuration

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
from django.conf.urls import url,include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import PasswordResetView,PasswordResetDoneView,PasswordResetConfirmView,PasswordResetCompleteView
from task import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.home_view,name='post-like'),
	url(r'^password_reset/', PasswordResetView.as_view(template_name='registration/password_reset.html'),name='password_reset'),
	url(r'^password_reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),name='password_reset_done'),
	url(r'^password_reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'),name='password_reset_confirm'),
	url(r'^password_reset-complete/', PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),name='password_reset_complete'),
    url(r'^Like/$', views.like_post,name='like-post'),
	url(r'^search/$',views.search_view),
	url(r'^(?P<id>\d+)/share/$',views.mail_view),
	url(r'^signup/',views.signup_view),
	url(r'^upload/$', views.upload_view),
	url(r'^(?P<id>\d+)/rate-post/$',views.rate,name='rate-post'),
	url(r'^accounts/',include('django.contrib.auth.urls')),
    url(r'^(?P<year>\d{4})/(?P<month>\d{2})/(?P<day>\d{2})/(?P<post>[-\w]+)/$', views.post_detail_view,name='post_detail'),

]+ static(settings.MEDIA_ROOT, document_root=settings.MEDIA_ROOT)



