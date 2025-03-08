from django.db import models
from customers.models import Customer
from tables.models import Table

class Reservation(models.Model):
    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("confirmed", "Confirmed"),
        ("canceled", "Canceled"),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # Клиент
    table = models.ForeignKey(Table, on_delete=models.CASCADE)  # Столик
    date = models.DateField()  # Дата бронирования
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default="pending")  # Статус брони
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания брони

    def __str__(self):
        return f"Reservation {self.id} - {self.status}"
