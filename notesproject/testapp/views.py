from django.shortcuts import render,get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from testapp.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from taggit.models import Tag

@login_required
def home_view(request,tag_slug=None):
	post_list=Post.objects.all()
	tag=None
	if tag_slug:
		tag=get_object_or_404(Tag,slug=tag_slug)
		post_list=post_list.filter(tags__in=[tag])

	paginator=Paginator(post_list,5)
	page_number=request.GET.get('page')
	try:
		post_list=paginator.page(page_number)
	except PageNotAnInteger:
		post_list=paginator.page(1)
	except EmptyPage:
		post_list=paginator.page(paginator.num_pages)
	return render(request,'testapp/home.html',{'post_list':post_list,'tag':tag})


from testapp.forms import CommentForm
@login_required
def post_view(request,year,month,day,post):
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
	return render(request,'testapp/page.html',{'post':post,'form':form,'csubmit':csubmit,'comments':comments})
	


from testapp.forms import SignupForm,EmailSendForm
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
	return render(request,'testapp/signup.html',{'form':form})

@login_required
def user_details(request):    
    user = get_object_or_404(User, id=request.user.id)    
    return render(request, 'testapp/profile.html', {'user': user})

@login_required
def update_view(request,id):
	user=User.objects.get(id=request.user.id)
	if request.method=='POST':
		form=SignupForm(request.POST,instance=user)
		if form.is_valid():
			user.save()
			form.save(commit=True)
			return redirect('/')
	return render(request,'testapp/details.html',{'user':user})

def logout_view(request):
	return render(request,'testapp/logout.html')

from django.contrib.auth.models import User
@login_required
def profile_view(request):
	return render(request,'testapp/profile.html')

@login_required
def details_view(request):
	return render(request,'testapp/details.html')

from django.core.mail import send_mail
@login_required
def mail_view(request,id):
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
	return render(request,'testapp/sharebymail.html',{'form':form,'post':post,'sent':sent})

@login_required
def side_view(request):
	return render(request,'testapp/sideblog.html')

from testapp.forms import PostForm
@login_required
def mypost_view(request):
	user=PostForm()
	if request.method=='POST':
		user=PostForm(request.POST)
		if user.is_valid():
			user.save()
	return render(request,'testapp/post.html',{'user':user})

@login_required
def myupload_view(request,id):
	user=User.objects.get(id=request.user.id)
	post = Post.objects.filter(author = user)
	total  = Post.objects.filter(author = user).count()
	return render(request,'testapp/myupload.html',{'user':user,'post_list':post,'total':total})

@login_required
def friends_view(request):
	user1 = User.objects.all()
	return render(request,'testapp/friend.html',{'user1':user1})

@login_required
def search_view(request):
	query=request.GET['query']
	post_list=Post.objects.filter(title__icontains=query)
	body_list=Post.objects.filter(body__icontains=query)
	if body_list:
		post_list=Post.objects.filter(body__icontains=query)
	return render(request,'testapp/search.html',{'post_list':post_list,'body_list':body_list})


@login_required
def allposts_view(request):
	return render(request,'testapp/getallposts.html')

def get_particular_view(request,id):
	post=get_object_or_404(Post,id=id)
	get_my_post = Post.objects.filter(author = post.author)
	total  = Post.objects.filter(author = post.author).count()
	return render(request,'testapp/getparticularpost.html',{'post':post,'get_my_post':get_my_post,'total':total})


