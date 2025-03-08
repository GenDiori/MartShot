from django.urls import path
from .views import (
    ReservationListView, ReservationCreateView,
    ReservationCreateAPIView, ReservationDetailAPIView, UserReservationsAPIView,
    ReservationUpdateAPIView, ReservationDeleteAPIView
)

urlpatterns = [
    # HTML маршруты
    path('', ReservationListView.as_view(), name='reservation-list'),  # ✅ Добавлено
    path('create/', ReservationCreateView.as_view(), name='reservation-create-html'),  # ✅ Добавлено

    # API маршруты
    path('api/', ReservationCreateAPIView.as_view(), name='reservation_create'),
    path('api/<int:pk>/', ReservationDetailAPIView.as_view(), name='reservation_detail'),
    path('api/user/<int:user_id>/', UserReservationsAPIView.as_view(), name='user_reservations'),
    path('api/<int:pk>/update/', ReservationUpdateAPIView.as_view(), name='reservation_update'),
    path('api/<int:pk>/delete/', ReservationDeleteAPIView.as_view(), name='reservation_delete'),
]
