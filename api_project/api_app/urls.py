from django.urls import path
from . import views

urlpatterns = [
    # Список статей (только чтение)
    path('v1/women/', views.WomenListAPIView.as_view(), name='api-women-list'),
    
    # Создание новой статьи
    path('v1/women/create/', views.WomenCreateAPIView.as_view(), name='api-women-create'),
    
    # Получение, обновление, удаление одной статьи по id
    path('v1/women/<int:pk>/', views.WomenRetrieveUpdateDestroyAPIView.as_view(), name='api-women-detail'),
    
    # Список категорий
    path('v1/categories/', views.CategoryListAPIView.as_view(), name='api-categories-list'),
    
    # Комбинированный эндпоинт (категории + статьи)
    path('v1/full/', views.FullDataAPIView.as_view(), name='api-full-data'),
]