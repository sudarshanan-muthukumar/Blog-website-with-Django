
from django.db import models
from django.urls import reverse, reverse_lazy
import datetime 

class Blog(models.Model):
    title  = models.CharField(max_length = 120)
    body   = models.TextField(max_length = 3000)
    author = models.ForeignKey('auth.user', on_delete = models.CASCADE, default = 1)
    date   = models.DateField(default=datetime.datetime.now())
        
    def __str__(self):
        return self.title[:50]
    
    def get_absolute_url(self):
        return reverse('blog_detail', args = [str(self.id)])
