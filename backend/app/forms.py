from django import forms
from .models import List_Book, Report

class BookForm(forms.ModelForm):
	class Meta:
		model = List_Book
		fields = ["author", "title", "isbn", "subject", "class_used"]

class ReportForm(forms.ModelForm):
	class Meta:
		model = Report
		fields = ["description"]

	def __init__(self, *args, **kwargs):
		super(ReportForm, self).__init__(*args, **kwargs)

		for visible in self.visible_fields():
			visible.field.widget.attrs['class'] = 'form-control'
