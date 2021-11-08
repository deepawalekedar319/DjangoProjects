from django import forms
class StudentRegistration(forms.Form):
	rollno=forms.IntegerField()
	name=forms.CharField()
	marks=forms.IntegerField()

