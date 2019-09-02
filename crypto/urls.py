from django.urls import include, path
from crypto import views

urlpatterns = [
    path('', views.home, name='crypto'),
    path('prices', views.prices, name='prices'),
]
