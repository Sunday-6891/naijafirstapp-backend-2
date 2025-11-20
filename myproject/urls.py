from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView

# ←←← JWT
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

# ←←← YOUR VIEWS (all from habits app now — cleaner!)
from habits.views import (
    RegisterView,        # ← Registration
    TodayTickView,       # ← Optional "Tick Today" button
    MyTicksView,         # ← Get all dates
    TickDateView,        # ← NEW: Manual tick any date + delete
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # ==================== AUTH & TICKS ====================
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),

    # Ticks
    path('api/ticks/', MyTicksView.as_view(), name='my-ticks'),                    # GET all ticked dates
    path('api/tick/', TickDateView.as_view(), name='tick-date'),                  # POST = tick any date, DELETE = untick
    path('api/tick/today/', TodayTickView.as_view(), name='tick-today'),          # optional quick today button

    # ←←← YOUR HOME PAGE (if you get auth.html)
    path('', TemplateView.as_view(template_name='auth.html'), name='home'),
]

