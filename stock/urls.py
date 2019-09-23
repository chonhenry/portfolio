from django.urls import include, path
from stock import views

urlpatterns = [
    path('', views.home, name='stock'),
    path('about/', views.about, name='about'),
    path('add_stock/', views.add_stock, name='add_stock'),
    path('delete/<stock_id>', views.delete, name='delete'),
    path('delete_stock', views.delete_stock, name='delete_stock'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]
