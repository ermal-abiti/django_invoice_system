from django import forms
from .models import *


class ShitjeForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		self.f_id = kwargs.pop('f_id')
		super(ShitjeForm, self).__init__(*args, **kwargs)
		self.fields['fletpercjellja'] = forms.ModelChoiceField(initial=self.f_id, queryset=Fletpercjellja.objects.all(), label='', widget=forms.Select(attrs={
				"style": "display:none;",
				"id": "fp_select",
				
			}))
	class Meta:
		model = Shitje
		fields = '__all__'
		# exclude = ('fletpercjellja',)


class SearchGetFletpercjellja(forms.Form):
	search = forms.CharField(label="Search", max_length=100)