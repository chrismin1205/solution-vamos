from django.urls import include, path

from . import views
# from result import views

urlpatterns = [
  path('', views.index, name='index'),
  # path('result/<int:pk>/', views.detail, name='detail')
  # path('result/', include('result.urls')),
]