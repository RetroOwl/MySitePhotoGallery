from django.db import models
from django.urls import reverse
from django.utils import timezone 
from django.contrib.auth.models import User

class PublishedManager(models.Manager):  
    def get_queryset(self):  
        return super(PublishedManager,  
		     self).get_queryset()\
                  .filter(status='published')

class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'), 
        ('published', 'Published'), 
    ) 
    title = models.CharField(max_length=255)
    publish = models.DateTimeField(u'Дата публикации') 
    content = models.TextField(max_length=10000)
    slug = models.SlugField(max_length=250, 
                            unique_for_date='publish',
                            default='publish')
    status = models.CharField(max_length=10, 
                              choices=STATUS_CHOICES, 
                              default='published')
    image = models.ImageField(default = 'temp.jpg', verbose_name = "Путь к картинке")
    
    def __str__(self):
        return self.title

    class Meta: 
        ordering = ('-publish',)

    objects = models.Manager() 
    published = PublishedManager() 

    def get_absolute_url(self):  
        return reverse('blog:post_detail',  
		       args=[self.publish.year,  
		       self.publish.month,  
		       self.publish.day,  
		       self.slug])

    


class Comment(models.Model):  
    post = models.ForeignKey(Post,  
			     on_delete=models.CASCADE,  
			     related_name='comments')  
    name = models.CharField(max_length=80)  
    email = models.EmailField()  
    body = models.TextField()  
    created = models.DateTimeField(auto_now_add=True)  
    updated = models.DateTimeField(auto_now=True)  
    active = models.BooleanField(default=True)  
      
    class Meta:  
        ordering = ('created',)  
          
    def __str__(self):  
        return 'Comment by {} on {}'.format(self.name, self.post)