from django import forms
from django.contrib.auth.models import User
from testapp.models import Comments,Post

class SignupForm(forms.ModelForm):
	first_name=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'fullname'}))
	username=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'username'}))
	email=forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'email'}))
	password=forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
	class Meta:
		model=User
		fields=['first_name','email','username','password']
		help_texts = {
            'username': None,
        }

class EmailSendForm(forms.Form):
	name=forms.CharField()
	email=forms.EmailField()
	to=forms.EmailField()
	comments=forms.CharField(required=False,widget=forms.Textarea)


class CommentForm(forms.ModelForm):
	class Meta:
		model=Comments
		fields=('name','email','body')

class PostForm(forms.ModelForm):
	class Meta:
		model=Post
		fields='__all__'
		help_texts = {
            'tag': None,
        }
