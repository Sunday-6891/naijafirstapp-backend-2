from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import RegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

# ←←← 1. REGISTER VIEW (SIGNUP)
class RegisterView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({
                'user': serializer.data,
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# ←←← 2. SECRET VIEW (PROTECTED)
class SecretView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        return Response({"secret": f"Hello {request.user.username}! 🚀"})