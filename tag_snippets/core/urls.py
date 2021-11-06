
from django.contrib import admin
from django.urls import path, include

from core import views

urlpatterns = [

    path('snippet/', views.SnippetView.as_view(), name='snippet'),
    path('snippet/<id>/', views.SnippetView.as_view(), name='snippet'),
    path('tag/', views.TagView.as_view(), name='tag'),
    path('tag/<id>/', views.TagView.as_view(), name='tag'),
]
