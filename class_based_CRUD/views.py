from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DeleteView, UpdateView, DetailView, CreateView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Book
from .forms import BookRegistration
from django.urls import reverse_lazy
from django.http import request
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import BookRegistration


@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
class BookListView(ListView):
    model = Book
    template_name = 'class_based/book-display.htm'
    context_object_name = 'books'

    def get_context_data(self,*args, **kwargs):
        books = self.get_queryset()
        paginator = Paginator(books,3)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        context = {'books': page_obj}
        return context


@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
class BookCreateView(CreateView):
    form_class = BookRegistration
    template_name = 'class_based/book-create.htm'
    success_url = reverse_lazy('book-list')


@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
class BookDeleteView(DeleteView):
    model = Book
    template_name = 'class_based/book-delete.htm'
    success_url = reverse_lazy('book-list')


@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
class BookUpdateView(UpdateView):
    model = Book
    template_name = 'class_based/book-update.htm'
    context_object_name = 'book'
    fields = ('name', 'isbn')
    success_url = reverse_lazy('book-list')


@method_decorator(login_required(login_url = 'user_login'), name='dispatch')
class BookDetailView(DetailView):
    model = Book
    template_name = 'class_based/book-detail.htm'
    context_object_name = 'book'
