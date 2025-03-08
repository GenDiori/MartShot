from django.contrib import admin
from .models import Table

@admin.register(Table)
class TableAdmin(admin.ModelAdmin):
    list_display = ('id', 'number', 'capacity', 'is_available')
    list_filter = ('is_available',)  # Фильтр по доступности
    search_fields = ('number',)  # Поиск по номеру столика
