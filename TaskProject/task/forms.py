from django import forms
from django.contrib.auth.models import User
from task.models import Post,Comments,Review, RATE_CHOICES

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
	name=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'Name'}))
	email=forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	to=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'To'}))
	comments=forms.CharField(label="",widget=forms.Textarea(attrs={'placeholder': 'Comments'}))


class CommentForm(forms.ModelForm):
	class Meta:
		model=Comments
		fields=('name','email','body')

class PostForm(forms.ModelForm):
	slug=forms.SlugField(label="Link")
	class Meta:
		model=Post
		fields='__all__'
		help_texts = {
            'tag': None,
        }

class RateForm(forms.ModelForm):
	rate = forms.ChoiceField(choices=RATE_CHOICES, widget=forms.RadioSelect(), required=True)

	class Meta:
		model = Review
		fields = ('rate',)