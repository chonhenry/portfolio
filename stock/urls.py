from django.urls import include, path
from stock import views

urlpatterns = [
    path('', views.home, name='stock'),
    path('about/', views.about, name='about'),
]
