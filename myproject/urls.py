from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from habits.views import RegisterView, TodayTickView, MyTicksView, TickDateView

urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),

    path('api/ticks/', MyTicksView.as_view(), name='my-ticks'),
    path('api/tick/', TickDateView.as_view(), name='tick-date'),
    path('api/tick/today/', TodayTickView.as_view(), name='tick-today'),
]



