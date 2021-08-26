from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

# TEST_DJANGO APP IMPORT
from test_django.models import UserRevised, Book
from test_django.forms import NameForm, UserCreateForm, BookCreateForm



# Create your views here.

def get_name(request):
    userList = UserRevised.objects
    
    return render(request, 'test_django/name.html', {'userList':userList})

class AccountCreateView(CreateView):
    model = UserRevised
    template_name = 'test_django/create.html'
    form_class = UserCreateForm
    success_url = reverse_lazy('testapp:login')


class BookCreateView(CreateView):
    model = Book
    template_name = 'test_django/createBook.html'
    form_class = BookCreateForm
    success_url = reverse_lazy('testapp:book')

def BookIndex(request):
    bookList = Book.objects
    target = None 
    if request.method == 'POST':
        target_title = request.POST.get("title")
        print("WARNING *********************")
        print(target_title)
        target = bookList.filter(title=target_title)
        print(target)

    return render(request, 'test_django/book.html', {'bookList':bookList, 'target':target})

class BookDetailView(DetailView):
    model = Book
    template_name = 'test_django/detailBook.html'
    context_object_name = 'target_book'

class BookListView(ListView):
    model = Book
    template_name = "test_django/listBook.html"
