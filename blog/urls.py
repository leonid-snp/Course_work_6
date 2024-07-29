from django.urls import path

from . import views
from blog.apps import BlogConfig

app_name = BlogConfig.name

urlpatterns = [
    path('create/', views.BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', views.BlogUpdateView.as_view(), name='update'),
    path('detail/<int:pk>/', views.BlogDetailView.as_view(), name='detail'),
    path('delete/<int:pk>/', views.BlogDeleteView.as_view(), name='delete'),
    path('list/', views.BlogListView.as_view(), name='list'),
]