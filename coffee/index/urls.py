from django.urls import path
from .views import index_view
urlpatterns = [
    path('', index_view, name='index'),
    # path('contact/', ContactFormView.as_view(), name='contact-form'),
]
