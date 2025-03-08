from django.contrib import admin
from .models import Customer

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')  # Отображаемые поля в списке
    search_fields = ('name', 'phone')  # Поиск по этим полям
