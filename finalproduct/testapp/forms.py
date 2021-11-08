from django import forms

class EmailSendForm(forms.Form):
	name =forms.CharField(label="____Name")
	email=forms.EmailField(label="____Email")
	to  =forms.EmailField(label="_______To")
	comments=forms.CharField(required=False,widget=forms.Textarea)

from testapp.models import Comments

class CommentForm(forms.ModelForm):
	class Meta:
		model=Comments
		fields=('name','email','body')