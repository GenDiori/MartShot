from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from .models import Customer
from .serializers import CustomerSerializer

# 📌 API: Получить список клиентов / Создать клиента
class CustomerListCreateView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# 📌 API: Получить данные конкретного клиента
class CustomerDetailView(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# 📌 HTML: Страница списка клиентов
def customer_list(request):
    customers = Customer.objects.all()
    return render(request, 'customers/list.html', {'customers': customers})

# 📌 HTML: Страница деталей клиента
def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return render(request, 'customers/detail.html', {'customer': customer})
