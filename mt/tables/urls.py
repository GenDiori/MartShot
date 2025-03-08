from django.urls import path
from .views import (
    TableListView, TableDetailView, TableCreateView,
    TableListCreateView, available_tables
)

urlpatterns = [
    # HTML маршруты
    path('', TableListView.as_view(), name='table-list'),  # Изменил для единого стиля
    path('<int:pk>/', TableDetailView.as_view(), name='table-detail'),
    path('create/', TableCreateView.as_view(), name='table-create'),  # Здесь изменено

    # API маршруты
    path('api/', TableListCreateView.as_view(), name='api-table-list-create'),  # Изменил для консистентности
    path('api/available/', available_tables, name='api-available-tables'),
]

