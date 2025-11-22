from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from habits.views import RegisterView

def api_root(request):
    return JsonResponse({
        'message': 'Habits Tracker API is running!',
        'endpoints': {
            'register': '/api/register/',
            'login': '/api/login/',
            'token_refresh': '/api/refresh/',
            'habits_api': '/api/',  # This now includes all habits endpoints
            'admin': '/admin/',
        }
    })

urlpatterns = [
    path('', api_root),  # Root endpoint - shows API info
    path('admin/', admin.site.urls),
    
    # Authentication endpoints
    path('api/register/', RegisterView.as_view(), name='register'),
    path('api/login/', TokenObtainPairView.as_view(), name='login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='refresh'),
    
    # Include habits app URLs under /api/
    path('api/', include('habits.urls')),
]



