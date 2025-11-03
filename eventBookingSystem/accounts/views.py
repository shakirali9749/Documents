from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import(
    SigninSerializer,
    SignupSerializer,
    UserProfileSerializer
)


class SignupView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self, request):
        serializer = SignupSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                "message": "User registered successfully!",
                "User": SignupSerializer(user).data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SigninView(APIView):
    permission_classes = [permissions.AllowAny]

    def post(self,request):
        serializer = SigninSerializer(data=request.data)
        if serializer.is_valid():
            return Response(
                {
                    "message": "login successfully!",
                    "access": serializer.validated_data["access"],
                    "refresh": serializer.validated_data["refresh"]
                },status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = UserProfileSerializer(request.user,context={"request": request})
        return Response(serializer.data)

    def patch(self, request):
        serializer = UserProfileSerializer(request.user, data=request.data, partial=True, context={"request": request})
        if serializer.is_valid():
            user = serializer.save()
            return Response({
                    "message": "User chagned successfully",
                    "user": UserProfileSerializer(user, context={"request": request}).data
                }, status=status.HTTP_200_OK
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




