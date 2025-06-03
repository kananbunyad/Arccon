from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
    path('contact/', views.contact, name='contact'),
    path('blog/', views.blog, name='blog'),
    path('team/', views.team, name='team'),
    path('projects/', views.projects, name='projects'),
    path('features/', views.features, name='features'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('projects/category/<str:category_name>/', views.projects_by_category, name='projects_by_category'),
]