from django import forms

class EmailSendForm(forms.Form):
	name = forms.CharField()
	email = forms.EmailField()
	to = forms.EmailField()
	comments=forms.CharField(required=False,widget=forms.Textarea)


from testapp.models import Comments
class CommentForm(forms.ModelForm):
	class Meta:
		model=Comments
		fields=('name','email','body')

from django.contrib.auth.models import User
class SignupForm(forms.ModelForm):
	first_name=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'fullname'}))
	last_name=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'lastname'}))
	username=forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder': 'username'}))
	email=forms.EmailField(label="",widget=forms.TextInput(attrs={'placeholder': 'email'}))
	password=forms.CharField(label="",widget=forms.PasswordInput(attrs={'placeholder': 'password'}))
	class Meta:
		model=User
		fields=['first_name','last_name','email','username','password']
		help_texts = {
		   'username': None,
		}

from testapp.models import Post
class UploadClass(forms.ModelForm):
	slug=forms.CharField(label="Image-link")
	class Meta:
		model=Post
		fields='__all__'
		help_texts = {
		'tag': None,
		}