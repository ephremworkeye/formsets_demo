from django.shortcuts import render
from django.contrib import messages
from django.views.generic import (TemplateView, ListView, CreateView, DetailView)

from .models import Author, Book

# Create your views here.

class HomeView(TemplateView):
    template_name = 'home.html'


class AuthorListView(ListView):
    model = Author
    template_name = 'author_list.html'

class AuthorDetailView(DetailView):
    model = Author
    template_name = 'author_detail.html'


class AuthorCreateView(CreateView):
    model = Author
    template_name = 'author_create.html'
    fields = ['name']

    def form_valid(self, form):
        messages.add_message(
            self.request,
            messages.SUCCESS,
            'The author has been added'
        )
        return super().form_valid(form)

    # def form_invalid(self, form):
    #     messages.add_message(
    #         self.request, 
    #         message.ERROR, 
    #         'There is an error. Try again'
    #         )
    #     return super().form_invalid(form)