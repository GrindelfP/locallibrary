from django.urls import path
from django.urls import re_path

from . import views

urlpatterns = [
    re_path(r'^$', views.index, name='index'),  # mb I should use path, not re_path
    re_path(r'^books/$', views.BookListView.as_view(), name='books'),
    re_path(r'^book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('author/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    re_path(r'^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    path(r'borrowed/', views.LoanedBooksAllListView.as_view(), name='all-borrowed')
]
