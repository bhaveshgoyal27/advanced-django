from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import FormView
from .models import Film, Commercial
from .forms import MovieSelectForm, FilmModelForm, CommercialModelForm
# Create your views here.

class MovieSelectForm(FormView):
	form_class = MovieSelectForm
	template_name = "movies/main.html"
	success_url = reverse_lazy("home")

	def post(self, *args, **kwargs):
		self.request.session["movie"] = sef.request.POST.get("movie")
		return super().post(*args, **kwargs)

class AddMovieForm(FormView):
	template_name = "movies/add.html"
	success_url = reverse_lazy("home")

	def get_form_class(self, *args, **kwargs):
		pass

