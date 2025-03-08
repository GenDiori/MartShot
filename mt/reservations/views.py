from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.utils.dateparse import parse_date
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Reservation
from .serializers import ReservationSerializer
from tables.models import Table
from customers.models import Customer

# 📌 API: Создать бронь с проверками
class ReservationCreateAPIView(generics.CreateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

    def create(self, request, *args, **kwargs):
        customer_id = request.data.get('customer')
        table_id = request.data.get('table')
        date = request.data.get('date')

        parsed_date = parse_date(date)
        if not parsed_date:
            return Response({'error': 'Invalid date format'}, status=status.HTTP_400_BAD_REQUEST)

        if Reservation.objects.filter(table=table_id, date=date).exists():
            return Response({'error': 'This table is already reserved for the selected date'}, status=status.HTTP_400_BAD_REQUEST)

        if Reservation.objects.filter(customer=customer_id, date=date).exists():
            return Response({'error': 'User already has a reservation on this date'}, status=status.HTTP_400_BAD_REQUEST)

        return super().create(request, *args, **kwargs)

# 📌 API: Получить детали брони
class ReservationDetailAPIView(generics.RetrieveAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# 📌 API: Получить список всех броней пользователя
class UserReservationsAPIView(APIView):
    def get(self, request, user_id):
        customer = get_object_or_404(Customer, id=user_id)
        reservations = Reservation.objects.filter(customer=customer)
        serializer = ReservationSerializer(reservations, many=True)
        return Response({'reservations': serializer.data})

# 📌 API: Обновить статус брони
class ReservationUpdateAPIView(generics.UpdateAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer

# 📌 API: Удалить бронь
class ReservationDeleteAPIView(generics.DestroyAPIView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
