from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from store.models import Product


class HomeStore(ListView):
    template_name = "home.html"
    model = Product
    context_object_name = 'catalogue_list'

