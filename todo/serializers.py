from rest_framework import serializers
from .models import Task, ContextEntry, Category

# Category Serializer
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# Task Serializer
class TaskSerializer(serializers.ModelSerializer):
    category = CategorySerializer(read_only=True)
    category_id = serializers.PrimaryKeyRelatedField(
        queryset=Category.objects.all(),
        source='category',
        write_only=True,
        required=False  # ✅ Makes it optional
    )

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'priority',
            'deadline',
            'status',
            'created_at',
            'updated_at',
            'category',
            'category_id'
        ]

# Context Entry Serializer
class ContextEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = ContextEntry
        fields = '__all__'
