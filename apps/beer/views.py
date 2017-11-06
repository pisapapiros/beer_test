from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from apps.beer.forms import BeerForm
from .models import Beer


class ListBeerView(ListView):
    model = Beer


class DetailBeerView(DetailView):
    model = Beer


class CreateBeerView(CreateView):
    model = Beer
    form_class = BeerForm
    success_url = reverse_lazy('list-beer')


class UpdateBeerView(UpdateView):
    model = Beer
    form_class = BeerForm
    success_url = reverse_lazy('list-beer')
