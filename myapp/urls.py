from django.urls import path
from .views import RegisterView, SecretView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    # ←←← YOUR JWT APIs
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('refresh/', TokenRefreshView.as_view(), name='refresh'),
    path('secret/', SecretView.as_view(), name='secret'),
]