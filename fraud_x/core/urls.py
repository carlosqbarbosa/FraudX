from django.views.generic import RedirectView
from django.urls import path
from .views import verify_transaction, index  # Agora importando index corretamente

urlpatterns = [
    path('', index, name='index'),  # Agora a função está importada corretamente
    path('verify_transaction/', verify_transaction, name='verify_transaction'),
     path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]


