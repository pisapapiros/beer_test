from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, ListView, DetailView

from .models import Bar


class ListBarView(ListView):
    model = Bar


class DetailBarView(DetailView):
    model = Bar


class CreateBarView(CreateView):
    model = Bar
    # form_class = BarForm
    fields = ['name']
    success_url = reverse_lazy('list-bar')


class UpdateBarView(UpdateView):
    model = Bar
    # form_class = BarForm
    fields = ['name']
    success_url = reverse_lazy('list-bar')