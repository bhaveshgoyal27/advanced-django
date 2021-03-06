from django import forms
from .models import Film, Commercial
from actors.models import Actor



MOVIE_CHOICES=(
	('FILM','Film'),
	('COMMERCIAL','Commercial'))

class MovieSelectForm(forms.Form):
	movie = forms.ChoiceField(choices =MOVIE_CHOICES, label="Choose your type", widget=forms.RadioSelect(attrs={}))


class FilmModelForm(forms.ModelForm):
	actors = forms.ModelMultipleChoiceField(label="Select all the actors", widget = forms.SelectMultiple, queryset=Actor.objects.filter(is_star=True))
	class Meta:
		model = Film
		fields = "__all__"

class CommercialModelForm(forms.ModelForm):
	actors = forms.ModelMultipleChoiceField(label="Select all the actors", widget = forms.SelectMultiple, queryset=Actor.objects.filter(is_star=False))
	class Meta:
		model = Commercial
		fields = "__all__"