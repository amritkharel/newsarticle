from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, DeleteView, ListView, UpdateView, DetailView
from .forms import ArticleCreationForm, ArticleUpdateForm
from .models import Article


class ArticleCreateView(LoginRequiredMixin, CreateView):
    form_class = ArticleCreationForm
    success_url = 'login'
    template_name = 'content/article_create.html'
    success_message = "Article has been created successfully"


    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class ArticleUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    form_class = ArticleUpdateForm
    success_url = 'login'
    template_name = 'content/article_update.html'
    success_message = "Article has been updated successfully"

    def test_func(self):
        if self.request.user == self.author:
            return True
        return False


class ArticleDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    template_name = 'content/article_delete.html'
    success_url = 'login'

    def test_func(self):
        if self.request.user == self.author:
            return True
        return False


class ArticleListView(ListView):
    model = Article
    template_name = 'content/article_list.html'
    context_object_name = 'articles'


class ArticleDetailView(DetailView):
    model = Article
    template_name = 'content/article_detail.html'
    context_object_name = 'article'
