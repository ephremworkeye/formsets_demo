from django.shortcuts import render
from django.views.generic import TemplateView, ListView
from .models import Author, Book

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'

class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'


