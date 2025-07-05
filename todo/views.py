from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Task, ContextEntry, Category
from .serializers import TaskSerializer, ContextEntrySerializer, CategorySerializer
from .ai_engine import suggest_priority, suggest_deadline, suggest_category, enhance_description

# Task APIs
class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all().order_by('-created_at')
    serializer_class = TaskSerializer

# Category APIs
class CategoryListView(generics.ListAPIView):
    queryset = Category.objects.all().order_by('-usage_count')
    serializer_class = CategorySerializer

# Context Entry APIs
class ContextListCreateView(generics.ListCreateAPIView):
    queryset = ContextEntry.objects.all().order_by('-created_at')
    serializer_class = ContextEntrySerializer
from .ai_engine import suggest_priority, suggest_deadline, suggest_category, enhance_description

@api_view(['POST'])
def get_ai_suggestions(request):
    task_title = request.data.get("title", "")
    task_description = request.data.get("description", "")
    context_entries = request.data.get("context", [])  # Pass a list

    # Call AI logic functions
    priority = suggest_priority(task_description, context_entries)
    deadline = suggest_deadline(task_description)
    category = suggest_category(task_description)
    enhanced_description = enhance_description(task_description, context_entries)

    return Response({
        "priority": priority,
        "deadline": deadline.strftime("%Y-%m-%dT%H:%M:%SZ"),
        "category": category,
        "enhanced_description": enhanced_description,
    })

from django.shortcuts import render

def dashboard_view(request):
    return render(request, 'dashboard.html')

def add_task_view(request):
    return render(request, 'add_task.html')

def add_context_view(request):
    return render(request, 'add_context.html')
