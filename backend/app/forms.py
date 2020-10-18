from django import forms
from .models import List_Book, Register

class BookForm(forms.ModelForm):
	class Meta:
		model = List_Book
		fields = ["author", "title", "isbn", "subject", "class_used"]