from django.shortcuts import render,get_object_or_404
from testapp.models import Post
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from testapp.forms import EmailSendForm
# implement mail nicely and even photo download
def home_view(request):
	post_list = Post.objects.all()
	paginator = Paginator(post_list,5)
	page_number = request.GET.get('page')
	try:
		post_list = paginator.page(page_number)
	except PageNotAnInteger:
		post_list = paginator.page(1)
	except EmptyPage:
		post_list = paginator.page(paginator.num_pages)
	return render(request,'testapp/home.html',{'post_list':post_list})

from testapp.forms import CommentForm
def post_detail_view(request , year , month , day , post): 
	pdf_provided = True
	image_provided = True
	post = get_object_or_404(Post , slug = post , status = 'published' , publish__year = year, publish__month = month, publish__day = day)
	image = post.image
	if image == 'No image':
		image_provided = False
	pdf = post.notesfiles
	if pdf == 'no pdf':
		pdf_provided = False	
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
	return render(request , 'testapp/post_detail.html',{'post':post,'pdf':pdf_provided,'image':image_provided,'form':form,'csubmit':csubmit,'comments':comments})

from django.core.mail import send_mail
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

def images_view(request):
	images=Post.objects.exclude(image__exact='No image')
	return render(request,'testapp/images.html',{'images':images})

def pdfs_view(request):
	pdfs=Post.objects.exclude(notesfiles__exact='no pdf')
	return render(request,'testapp/pdfs.html',{'pdfs':pdfs})

def get_particular_view(request,id):
	post=get_object_or_404(Post,id=id)
	allposts = Post.objects.filter(author = post.author)
	total  = Post.objects.filter(author = post.author).count()
	return render(request,'testapp/particularuser.html',{'post':post,'allposts':allposts,'total':total})

def search_view(request):
	query=request.GET['query']
	post_list=Post.objects.filter(title__icontains=query)
	body_list=Post.objects.filter(body__icontains=query)
	if body_list:
		post_list=Post.objects.filter(body__icontains=query)
	return render(request,'testapp/search.html',{'post_list':post_list,'body_list':body_list})