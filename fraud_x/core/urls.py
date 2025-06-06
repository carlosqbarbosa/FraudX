from django.views.generic import RedirectView
from django.urls import path
from .views import verify_transaction, index

urlpatterns = [
    path('', index, name='index'),
    path('verify_transaction/', verify_transaction, name='verify_transaction'),
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]


