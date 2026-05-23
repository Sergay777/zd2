import sys
import os
import django

# Настройка окружения Django (чтобы скрипт видел модели)
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api_project.settings')
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
django.setup()

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from io import BytesIO
from api_app.serializers import WomenManualSerializer
from api_app.models import Category, Women

# 1. Создаём тестовую категорию, если её нет
cat, created = Category.objects.get_or_create(name="Тестовая категория")
print(f"📌 Категория: {cat.name} (id={cat.id})")

# 2. Данные для создания новой статьи
data = {
    'title': 'Статья из демо-скрипта',
    'content': 'Это содержимое, созданное через сериализатор.',
    'is_published': True,
    'cat_id': cat.id,
}

# 3. Десериализация: проверяем данные
serializer = WomenManualSerializer(data=data)
print("\n🔍 Проверка валидации...")
if serializer.is_valid():
    print("✅ Данные валидны")
    print("📄 validated_data:", serializer.validated_data)
else:
    print("❌ Ошибки:", serializer.errors)
    exit()

# 4. Сохранение (вызовет create в сериализаторе)
instance = serializer.save()
print(f"\n💾 Создана статья: {instance.title} (id={instance.id})")

# 5. Сериализация объекта обратно в словарь
serializer2 = WomenManualSerializer(instance)
print("\n📦 serializer.data (после сохранения):", serializer2.data)

# 6. Преобразование в JSON-байты
json_bytes = JSONRenderer().render(serializer2.data)
print("\n🔷 JSON-байты:", json_bytes[:100], "...")  # показываем начало

# 7. Обратное преобразование из байтов в словарь через JSONParser
stream = BytesIO(json_bytes)
parsed_data = JSONParser().parse(stream)
print("\n🔄 Распарсенные данные из JSON:", parsed_data)

# 8. Демонстрация ошибки валидации (несуществующая категория)
print("\n⚠️ Проверка ошибки валидации (cat_id=99999):")
invalid_data = {
    'title': 'Неверная статья',
    'content': '...',
    'is_published': True,
    'cat_id': 99999,
}
invalid_serializer = WomenManualSerializer(data=invalid_data)
if not invalid_serializer.is_valid():
    print("❌ Ошибки:", invalid_serializer.errors)

print("\n✅ Демонстрация завершена.")