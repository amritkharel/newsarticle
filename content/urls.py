from django.urls import path
from .views import ArticleCreateView, ArticleUpdateView, ArticleListView, ArticleDeleteView, ArticleDetailView

urlpatterns = [
    path('news/', ArticleListView.as_view(), name='home'),
    path('news/add/', ArticleCreateView.as_view(), name='create'),
    path('news/detail/<int:pk>', ArticleDetailView.as_view(), name='detail'),
    path('news/update/<int:pk>/', ArticleUpdateView.as_view(), name='update'),
    path('news/delete/<int:pk>/', ArticleDeleteView.as_view(), name='delete'),
]