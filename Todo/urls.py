from django.urls import path
from django.contrib.auth import views as auth_views
from .views import PostListView,PostDetailView

from . import views
urlpatterns = [
    path('', PostListView.as_view(),name='home'),
    path('post/<int:pk>/', PostDetailView.as_view(),name='detail')
]