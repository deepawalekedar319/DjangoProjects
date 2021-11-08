from django.shortcuts import render,get_object_or_404
from testapp.models import Post
from taggit.models import Tag
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

def post_list_view(request,tag_slug=None):
	post_list=Post.objects.all()
	tag=None
	if tag_slug:
		tag=get_object_or_404(Tag,slug=tag_slug)
		post_list=post_list.filter(tags__in=[tag])
	return render(request,'testapp/base.html',{'post_list':post_list,'tag':tag})

from testapp.forms import CommentForm
def post_detail(request,year,month,day,post):
	post=get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
	comments=post.comments.filter(active=True)
	csubmit=False
	if request.method=='POST':
		form=CommentForm(request.POST)
		if form.is_valid():
			new_comment=form.save(commit=False)
			new_comment.post=post
			new_comment.save()
			csubmit=True
	else:
		form=CommentForm()
	return render(request,'testapp/sharespecificimage.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})

	
from django.core.mail import send_mail
from testapp.forms import *

def mail_send_view(request,id):
	post=get_object_or_404(Post,id=id,status='published')
	sent=False
	if request.method=='POST':
		form=EmailSendForm(request.POST)
		if form.is_valid():
			cd=form.cleaned_data
			subject='{}({}) recommends you to read"{}"'.format(cd['name'],cd['email'],post.title)
			post_url=request.build_absolute_uri(post.get_absolute_url())
			message='Read Post At:\n {}\n\n{}\'s Comments:\n{}'.format(post_url,cd['name'],cd['comments'])
			send_mail(subject,message,'notes@blog.com',[cd['to']])
			sent=True
	else:
		form=EmailSendForm()
	return render(request,'testapp/sharemail.html',{'form':form,'post':post,'sent':sent})

@login_required
def upload_view(request):
	user=UploadClass()
	if request.method=='POST':
		user=UploadClass(request.POST,request.FILES)
		if user.is_valid():
			user.save()
	return render(request,'testapp/upload.html',{'user':user})

def search_view(request):
	query=request.GET['query']
	post_list=Post.objects.filter(title__icontains=query)
	body_list=Post.objects.filter(body__icontains=query)
	if body_list:
		post_list=Post.objects.filter(body__icontains=query)
	return render(request,'testapp/search.html',{'post_list':post_list,'body_list':body_list})

def logout_view(request):
	return render(request,'registration/logout.html')

from testapp.forms import SignupForm
def signup_view(request):
	form=SignupForm()
	if request.method=='POST':
		form=SignupForm(request.POST)
		if form.is_valid():
			form.save()
			user=form.save()
			user.set_password(user.password)
			user.save()
			form.save()
			return HttpResponseRedirect('/accounts/login')
	return render(request,'registration/signup.html',{'form':form})


@login_required
def update_view(request,id):
	user=User.objects.get(id=request.user.id)
	images = Post.objects.filter(author = user)
	total  = Post.objects.filter(author = user).count()
	return render(request,'testapp/details.html',{'user':user,'images':images,'total':total})

def get_particular_view(request,id):
	post=get_object_or_404(Post,id=id)
	images = Post.objects.filter(author = post.author)
	total  = Post.objects.filter(author = post.author).count()
	return render(request,'testapp/particularuser.html',{'post':post,'images':images,'total':total})
