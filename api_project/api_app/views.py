from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women, Category
from .serializers import CategorySerializer, CombinedDataSerializer, WomenManualSerializer

class WomenListAPIView(generics.ListAPIView):
    queryset = Women.objects.filter(is_published=True)
    serializer_class = WomenManualSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FullDataAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        women = Women.objects.filter(is_published=True)
        serializer = CombinedDataSerializer({
            'categories': categories,
            'women': women
        })
        return Response(serializer.data)
    
class WomenCreateAPIView(generics.CreateAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenManualSerializer

class WomenRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Women.objects.all()
    serializer_class = WomenManualSerializer