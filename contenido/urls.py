from django.urls import path
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views



urlpatterns = [
    path('blog_detail/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),

]
