from django.urls import path
from .views import blogListView, blogDetailView

urlpatterns = [
    path('post/<int:pk>/', blogDetailView.as_view(), name='post_detail'),
    path('', blogListView.as_view(), name='home'),
]
