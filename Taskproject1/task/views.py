from django.shortcuts import render,get_object_or_404,redirect
from task import models
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required

def home_view(request):
	post_list = models.Post.objects.all()
	paginator=Paginator(post_list,5)
	user = request.user
	page_number=request.GET.get('page')
	try:
		post_list=paginator.page(page_number)
	except PageNotAnInteger:
		post_list=paginator.page(1)
	except EmptyPage:
		post_list=paginator.page(paginator.num_pages)
	return render(request,'task/home.html',{'post_list':post_list,'user':user})

@login_required
def like_post(request):
	user = request.user
	if request.method=='POST':
		post_id=request.POST.get('post_id')
		post_obj = models.Post.objects.get(id=post_id)

		if user in post_obj.liked.all():
			post_obj.liked.remove(user)
		else:
			post_obj.liked.add(user)
		
		like,created = models.Like.objects.get_or_create(user=user,post_id=post_id)

		if not created:
			if like.value=='Like':
				like.value='Unlike'
			else:
				like.value='Like'
		like.save()
	return redirect('post-like')

from task.forms import CommentForm,RateForm,PostForm

def post_detail_view(request,year,month,day,post):
	post=get_object_or_404(models.Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
	rate=models.Review.objects.all()
	sum=0
	for r in rate:
		if r.post==post:
			sum=(sum+r.rate)/10
	rate=round(sum,2)	
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
	return render(request,'task/post_detail.html',{'post':post,'rate':rate,'form':form,'csubmit':csubmit,'comments':comments})
	
from django.core.mail import send_mail
from task.forms import EmailSendForm 
@login_required
def mail_view(request,id):
	post=get_object_or_404(models.Post,id=id,status='published')
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
	return render(request,'task/sharebymail.html',{'form':form,'post':post,'sent':sent})


from django.http import HttpResponseRedirect
@login_required
def rate(request, id):
	post = models.Post.objects.get(id=id)
	user = request.user
	if request.method == 'POST':
		form = RateForm(request.POST)
		if form.is_valid():
			rate = form.save(commit=False)
			rate.user = user
			rate.post = post
			rate.save()
			return HttpResponseRedirect(reverse('post-like',))
	else:
		form = RateForm()
	return render(request,'task/rate.html',	{'form': form, 'post': post,})


def search_view(request):
	query=request.GET['query']
	post_list=models.Post.objects.filter(title__icontains=query)
	body_list=models.Post.objects.filter(body__icontains=query)
	if body_list:
		post_list=models.Post.objects.filter(body__icontains=query)
	return render(request,'task/search.html',{'post_list':post_list,'body_list':body_list})

from task.forms import SignupForm
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
def upload_view(request):
	user=PostForm()
	if request.method=='POST':
		user=PostForm(request.POST)
		if user.is_valid():
			user.save()
			return redirect('/')
	return render(request,'task/upload.html',{'user':user})