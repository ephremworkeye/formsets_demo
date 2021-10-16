from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),

]