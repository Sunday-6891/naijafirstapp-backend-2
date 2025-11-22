# habits/urls.py
from django.urls import path
from .views import TodayTickView, MyTicksView, TickDateView

urlpatterns = [
    path('ticks/', MyTicksView.as_view(), name='my-ticks'),
    path('tick/', TickDateView.as_view(), name='tick-date'),
    path('tick/today/', TodayTickView.as_view(), name='tick-today'),
]