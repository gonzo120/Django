from django.urls import path
from . import views
urlpatterns = [
     path('home/<str:username>', views.hello),
     path('', views.index),
     path('about/', views.about),
     path('projects/', views.projects),
     path('tasks/', views.tasks)
]