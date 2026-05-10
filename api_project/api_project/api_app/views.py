from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Women, Category
from .serializers import WomenSerializer, CategorySerializer, CombinedDataSerializer

class WomenListAPIView(generics.ListAPIView):
    queryset = Women.objects.filter(is_published=True)
    serializer_class = WomenSerializer

class CategoryListAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

class FullDataAPIView(APIView):
    def get(self, request):
        categories = Category.objects.all()
        women = Women.objects.filter(is_published=True)
        
        data = {
            'categories': CategorySerializer(categories, many=True).data,
            'women': WomenSerializer(women, many=True).data
        }
        return Response(data)