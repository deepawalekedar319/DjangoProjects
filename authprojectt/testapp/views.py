from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# Create your views here.
@login_required
def update_view(request):
	return render(request,'testapp/base_auth.html')

@login_required
def home_view(request):
	return render(request,'testapp/home.html')

@login_required
def java_view(request):
	return render(request,'testapp/java.html')

@login_required
def python_view(request):
	return render(request,'testapp/python.html')

def signin_view(request):

	return render(request,'testapp/signup.html')

def logout_view(request):
	return render(request,'testapp/logout.html')