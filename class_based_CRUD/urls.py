from django.urls import path
from class_based_CRUD import views

urlpatterns = [
   path('',views.BookListView.as_view(), name='book-list'),
   path('<int:pk>/update', views.BookUpdateView.as_view(), name='book-update'),
   path('create', views.BookCreateView.as_view(), name='book-create'),
   path('<int:pk>/delete', views.BookDeleteView.as_view(), name='book-delete'),
   path('detail/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]
