"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path

from blogapp import views
from blogapp.views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from blogproject import settings
from django.conf.urls.static import static
from users import views as user_views
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('admin/', admin.site.urls),
    # path('home',views.home,name='home'),
    path('about',views.about,name='about'),
    path('',PostListView.as_view(),name="home"),
    path('post/new', PostCreateView.as_view(template_name='blog/post_form.html'), name="blog-new"),
    path('post/<int:pk>/', PostDetailView.as_view(template_name='blog/post_detail.html'),name='blog-detail'),
    path('post/<int:pk>/update', PostUpdateView.as_view(template_name='blog/post_form.html'), name='blog-update'),
    path('post/<int:pk>/delete', PostDeleteView.as_view(template_name='blog/post_delete.html'), name='blog-delete'),

    path('register/', user_views.register, name="register"),
    path('profile/',user_views.profile,name='profile'),
    path('profile/profile_update/',user_views.profile_update,name='profile-update'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name="login"),
    path('logout/', auth_views.LoginView.as_view(template_name='users/logout.html'), name="logout"),

]




if settings.DEBUG:
   urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
   urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)