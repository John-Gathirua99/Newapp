from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView,DetailView,DeleteView,UpdateView,CreateView

from .models import PostModel
def home(request):    
    posts = PostModel.objects.all()
    context = {'posts':posts}
    return render(request,'Todo/home.html',context)


class PostListView(ListView):
    model = PostModel
    context_object_name='posts'
    template_name = 'todo/home.html'


class PostDetailView(DetailView):
    model = PostModel
    # context_object_name = 'post'
    template_name = 'todo/detail.html'