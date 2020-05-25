"""
Definition of views.
"""

from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime

from blog.models import Post, Comment
from blog.forms import CommentForm
from django.views.generic import ListView, DetailView

from django.views.generic.edit import FormView
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login

from django.http import HttpResponseRedirect
from django.views.generic.base import View
from django.contrib.auth import logout

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blog/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

class RegisterFormView(FormView):
    form_class = UserCreationForm

    success_url = "/login/"

    template_name = "blog/register.html"

    def form_valid(self, form):
        
        form.save()

        return super(RegisterFormView, self).form_valid(form)

class LoginFormView(FormView):
    form_class = AuthenticationForm
   
    template_name = "blog/login.html"
    
    success_url = "/"

    def form_valid(self, form):      
        self.user = form.get_user()        
        login(self.request, self.user)
        return super(LoginFormView, self).form_valid(form)

class LogoutView(View):
    def get(self, request):        
        logout(request)
        return HttpResponseRedirect("/")

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blog/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'blog/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )

def post_list(request): 
      posts = Post.published.all()
      return render(request, 
	                'blog/post/list.html', 
	                {'posts': posts})                

def post_detail(request, year, month, day, post):  
    post = get_object_or_404(Post, slug=post,  
				   status='published',  
				   publish__year=year,  
				   publish__month=month,  
				   publish__day=day)  
      
    
    comments = post.comments.filter(active=True)  
    new_comment = None  
    if request.method == 'POST':  
        
        comment_form = CommentForm(data=request.POST)  
        if comment_form.is_valid():  
            
            new_comment = comment_form.save(commit=False)  
            
            new_comment.post = post  
            
            new_comment.save()  
    else:  
        comment_form = CommentForm()  
    return render(request,  
		  'blog/post/detail.html',  
		  {'post': post,  
		  'comments': comments,  
		  'new_comment': new_comment,  
		  'comment_form': comment_form})

class PostDetailView(DetailView):
    model = Post


