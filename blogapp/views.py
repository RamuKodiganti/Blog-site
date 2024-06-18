from django.shortcuts import render, redirect
from django.views import View
from .models import Article
from django.views.generic import ListView, DetailView, DeleteView  # Class-based view provided by Django's generic views system. It is used to display a list of objects from a database model in a template simplifies the process of fetching the data from the database, paginating the results, and rendering the data in a template.
from django.urls import reverse_lazy

# Create your views here.

class Index(ListView):
    model = Article
    queryset = Article.objects.all().order_by('-date')
    template_name = 'blogapp/index.html'

class Featured(ListView):
    model = Article
    queryset = Article.objects.filter(featured=True).order_by('-date')
    template_name = 'blogapp/featured.html'

class DetailArticleView(DetailView):
    model = Article
    template_name = 'blogapp/blog_post.html'

    def get_context_data(self,*args,**kwargs):
        context = super(DetailArticleView,self).get_context_data(*args,**kwargs)
        context['liked_by_user'] = False
        article = Article.objects.get(id=self.kwargs.get('pk'))
        if article.likes.filter(pk=self.request.user.id).exists():
            context['liked_by_user'] = True
        return context
    
class LikeArticle(View):
    def post(self,request,pk):
        article = Article.objects.get(id=pk)

        if article.likes.filter(pk=self.request.user.id).exists():
            article.likes.remove(self.request.user.id)
        else:
            article.likes.add(self.request.user.id)

        article.save()
        return redirect('detail_article',pk)

class DeleteArticleView(DeleteView):
    model = Article
    template_name = 'blogapp/blog_delete.html'
    success_url = reverse_lazy('index')