from django.urls import path
from test_django.views import get_name
from django.views.generic import TemplateView

app_name="testapp"
urlpatterns = [
    path('', get_name, name='testForm'),
    path('thanks/', TemplateView.as_view(template_name="test_django/thank.html"), name="resultForm"),
]