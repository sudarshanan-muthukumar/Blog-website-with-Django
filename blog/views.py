from django.shortcuts import render            
from .models import Blog
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin 
from django.core.exceptions import PermissionDenied  
from .forms import UpdateBlog



from django.views.generic import(
    ListView,
    DetailView
)

from django.views.generic.edit import(
    CreateView,
    UpdateView,
    DeleteView,
)

class BlogList(LoginRequiredMixin,ListView):
    model         = Blog
    template_name = "blog_list.html"
    login_url     = 'login'
    
    def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            context['object_list'] = Blog.objects.all()[::-1]
            return context
        

class BlogDetail(LoginRequiredMixin, DetailView):
    model         = Blog
    template_name = "blog_detail.html"
    login_url     = 'login'

class BlogCreate(LoginRequiredMixin, CreateView):
    model          = Blog
    template_name  = "blog_new.html"
    form_class    = UpdateBlog                         
    success_url    = reverse_lazy("blog_list")
    login_url      = 'login'
    
   
class BlogUpdate(LoginRequiredMixin, UpdateView):
    model         = Blog
    template_name = "blog_update.html"                   
    form_class    = UpdateBlog                    
    login_url     = 'login'
    
    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)


class BlogDelete(LoginRequiredMixin, DeleteView):
    model         = Blog
    template_name = "blog_delete.html"
    success_url   = reverse_lazy("blog_list")
    login_url     = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)
        

class SearchView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = 'search_blogs.html'
    login_url = 'login'

    def get_queryset(self):
        query = self.request.GET.get('q')
        if query:
            object_list = self.model.objects.filter(title__icontains=query)
        elif query is not None:
                object_list = self.model.objects.none()
        return object_list