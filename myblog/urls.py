from django.urls import include, path
from myblog import views

app_name = 'myblog'

urlpatterns = [
    #path('', views.home, name='home'),
    path('', views.PostListView.as_view(), name='home'),
    path('post/<int:pk>/', views.PostDetailView.as_view(), name='detail'),
    path('create/', views.PostCreateView.as_view(), name='create'),
]
