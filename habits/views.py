from django.shortcuts import render

# Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .models import Tick
from django.utils import timezone
from datetime import date, datetime

# ==================== REGISTRATION ====================
class RegisterView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        email = request.data.get('email', '')

        if not username or not password:
            return Response({"error": "Username and password are required"}, status=status.HTTP_400_BAD_REQUEST)

        if User.objects.filter(username=username).exists():
            return Response({"error": "Username already taken"}, status=status.HTTP_400_BAD_REQUEST)

        user = User.objects.create_user(username=username, email=email, password=password)
        refresh = RefreshToken.for_user(user)

        return Response({
            "message": "Account created successfully!",
            "access": str(refresh.access_token),
            "refresh": str(refresh)
        }, status=status.HTTP_201_CREATED)


# ==================== MANUAL TICK ANY DATE ====================
class TickDateView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        date_str = request.data.get('date')  # expect "YYYY-MM-DD"
        if not date_str:
            return Response({"error": "Date is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            tick_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "Invalid date format. Use YYYY-MM-DD"}, status=status.HTTP_400_BAD_REQUEST)

        tick, created = Tick.objects.get_or_create(user=request.user, date=tick_date)
        if created:
            return Response({"message": "Ticked!", "date": date_str}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": "Already ticked"}, status=status.HTTP_200_OK)

    def delete(self, request):
        date_str = request.data.get('date')
        if not date_str:
            return Response({"error": "Date is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            tick_date = datetime.strptime(date_str, "%Y-%m-%d").date()
        except ValueError:
            return Response({"error": "Invalid date format"}, status=status.HTTP_400_BAD_REQUEST)

        deleted = Tick.objects.filter(user=request.user, date=tick_date).delete()
        if deleted[0] > 0:
            return Response({"message": "Unticked"}, status=status.HTTP_200_OK)
        return Response({"message": "No tick found"}, status=status.HTTP_404_NOT_FOUND)


# ==================== GET ALL TICKS ====================
class MyTicksView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        ticks = Tick.objects.filter(user=request.user).values_list('date', flat=True)
        dates = [d.strftime("%Y-%m-%d") for d in ticks]
        return Response({"dates": dates})


# ==================== TODAY TICK (optional, keep if you want button) ====================
class TodayTickView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request):
        today = date.today()
        tick, created = Tick.objects.get_or_create(user=request.user, date=today)
        if created:
            return Response({"message": "Ticked today! ✓"}, status=status.HTTP_201_CREATED)
        return Response({"message": "Already ticked today"})