from django.shortcuts import render
from testapp.models import *
def about_view(request):
	return render(request,'testapp/about.html')

def home_view(request):
	cats = Category.objects.all()
	images = Image.objects.all()
	return render(request,'testapp/base.html',{'images':images,'cats':cats})

def category_view(request,id):
	cats = Category.objects.all()
	category = Category.objects.get(id = id)
	images = Image.objects.filter(cat=category)
	return render(request,'testapp/base.html',{'images':images,'cats':cats})
