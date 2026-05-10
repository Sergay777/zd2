from django.urls import path
from . import views

urlpatterns = [
    path('v1/women/', views.WomenListAPIView.as_view(), name='api-women-list'),
    path('v1/categories/', views.CategoryListAPIView.as_view(), name='api-categories-list'),
    path('v1/full/', views.FullDataAPIView.as_view(), name='api-full-data'),  
]