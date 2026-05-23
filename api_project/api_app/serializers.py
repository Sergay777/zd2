from rest_framework import serializers
from .models import Women, Category

# ---------- Ручной сериализатор (полный контроль) ----------
class WomenManualSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    title = serializers.CharField(max_length=255)
    content = serializers.CharField(required=False, allow_blank=True)
    is_published = serializers.BooleanField(default=True)
    cat_id = serializers.IntegerField()
    time_create = serializers.DateTimeField(read_only=True)
    time_update = serializers.DateTimeField(read_only=True)

    def validate_cat_id(self, value):
        if not Category.objects.filter(id=value).exists():
            raise serializers.ValidationError("Категория с таким id не существует")
        return value

    def create(self, validated_data):
        cat_id = validated_data.pop('cat_id')
        category = Category.objects.get(id=cat_id)
        return Women.objects.create(cat=category, **validated_data)

    def update(self, instance, validated_data):
        instance.title = validated_data.get('title', instance.title)
        instance.content = validated_data.get('content', instance.content)
        instance.is_published = validated_data.get('is_published', instance.is_published)
        if 'cat_id' in validated_data:
            cat_id = validated_data['cat_id']
            instance.cat = Category.objects.get(id=cat_id)
        instance.save()
        return instance


# ---------- ModelSerializer (быстрый старт) ----------
class WomenModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ['id', 'title', 'content', 'is_published', 'cat', 'time_create', 'time_update']
        read_only_fields = ['id', 'time_create', 'time_update']