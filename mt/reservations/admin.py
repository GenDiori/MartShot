from django.contrib import admin
from .models import Reservation

@admin.register(Reservation)
class ReservationAdmin(admin.ModelAdmin):
    list_display = ('id', 'customer', 'table', 'date', 'status', 'created_at')
    list_filter = ('status', 'date')  # Фильтр по статусу и дате
    search_fields = ('customer__name', 'table__number')  # Поиск по клиенту и столику
