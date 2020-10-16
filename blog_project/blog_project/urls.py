"""blog_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path

from blog.views import PostDetailView, PostListView
from config.views import links
from blog_project.custom_site import custom_site

urlpatterns = [
    path(r'', PostListView.as_view(),name='index'),
    path(r'super_admin/', admin.site.urls,name='super-admin'),
    path(r'admin/', custom_site.urls,name='admin'),
    path(r'category/<int:category_id>/',PostListView.as_view(),name='category-list'),
    path(r'tag/<int:tag_id>/',PostListView.as_view(),name='tag-list'),
    # re_path(r'post/(?P<post_id>\d+).html',post_detail,name='post-detail'), #django 2 正则re_path或者不使用正则直接指定类型
    path(r'links/',links,name='links'),
    re_path(r'post/(?P<pk>\d+).html',PostDetailView.as_view(),name='post-detail'),

]
