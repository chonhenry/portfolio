from django.urls import include, path
from stock import views

urlpatterns = [
    path('', views.home, name='stock'),
    path('about/', views.about, name='about'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name='delete'),
]
