from django.urls import path

from . import views
urlpatterns = [

    # homepage
    path('', views.home.as_view(), name='home'),

    # about page
    path('about/', views.about.as_view(), name='about'),

    # contact page
    path('contact/', views.contact.as_view(), name='contact'),

    # particular blog page
    path('post/<int:id>/', views.blog_post.as_view(), name='blog_post'),

]
