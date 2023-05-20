from django.urls import path
from . import views
from django.urls import re_path

urlpatterns = [
    re_path(r'^$', views.index, name='index'),  # mb I should use path, not re_path
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
]
