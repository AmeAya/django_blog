from django.views.generic import ListView, DetailView, CreateView

from .models import Post
# Create your views here.

class blogListView(ListView):
    model = Post
    template_name = 'home.html'

class blogDetailView(DetailView):
    model = Post
    template_name = 'post_detail.html'

class blogCreateView(CreateView):
    model = Post
    template_name = 'post_new.html'
    fields = ['title', 'author', 'body']
