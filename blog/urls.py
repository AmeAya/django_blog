from django.urls import path
from .views import blogListView

urlpatterns = [
    path('', blogListView.as_view(), name='home'),
]
