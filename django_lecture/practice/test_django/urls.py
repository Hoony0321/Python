from django.urls import path
from test_django.views import get_name, AccountCreateView, BookCreateView, BookIndex, BookDetailView, BookListView
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView


app_name="testapp"
urlpatterns = [
    path('', get_name, name='get_name'),
    path('thanks/', TemplateView.as_view(template_name="test_django/thank.html"), name="resultForm"),
    path('create/', AccountCreateView.as_view(), name='create'),
    path('login/', LoginView.as_view(template_name="test_django/login.html"), name='login'),
    path('createBook/', BookCreateView.as_view(), name="createBook"),
    path('book/', BookIndex, name='book' ),
    path('detailBook/<int:pk>', BookDetailView.as_view(), name="detailBook"),
    path('listBook/', BookListView.as_view(), name="listBook"),
]