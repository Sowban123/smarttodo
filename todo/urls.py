from django.urls import path
from .views import TaskListCreateView, CategoryListView, ContextListCreateView, get_ai_suggestions
from .views import dashboard_view, add_task_view, add_context_view

urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('categories/', CategoryListView.as_view(), name='category-list'),
    path('context/', ContextListCreateView.as_view(), name='context-list-create'),
    path('ai/suggestions/', get_ai_suggestions, name='ai-suggestions'),
    path('', dashboard_view, name='dashboard'),
    path('add-task/', add_task_view, name='add-task'),
    path('add-context/', add_context_view, name='add-context'),
]
