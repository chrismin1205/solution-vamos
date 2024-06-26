from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='result'),
  path('search_result/', views.search_result, name='search_result'),
  path('<int:pk>/', views.detail, name='detail')
]