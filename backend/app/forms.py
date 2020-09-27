from django import forms
from .models import Login, List_Book

class LoginForm(forms.ModelForm):
	class Meta:
		model = Login
		fields = ["sjsu_id", "sjsu_pw"]

class BookForm(forms.ModelForm):
	class Meta:
		model = List_Book
		fields = ["author", "title", "isbn", "subject", "class_used"]