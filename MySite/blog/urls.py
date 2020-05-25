
from django.urls import path
from . import views
from blog.views import PostDetailView 

app_name = 'blog' 

urlpatterns = [    
    path('', views.post_list, name='post_list'),
    #url(r'^(?P<pk>\d+)/$', PostDetailView.as_view()),
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.post_detail, name='post_detail'),
]