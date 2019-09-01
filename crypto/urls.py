from django.urls import include, path
from crypto import views

urlpatterns = [
    path('', views.hometest),
]
