from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('authors/', views.AuthorListView.as_view(), name='list_authors'),
    path('authors/add', views.AuthorCreateView.as_view(), name='author_add'),
    path('authors/<int:pk>/', views.AuthorDetailView.as_view(), name='author_detail'),

]