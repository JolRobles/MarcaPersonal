from django.urls import path
from django.conf.urls import url
from home import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path(r'', views.index, name='index'),

]