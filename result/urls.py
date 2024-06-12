from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='result'),
  path('<int:work_id>/', views.detail, name='detail')
]