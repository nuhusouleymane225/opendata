from rest_framework import viewsets, generics
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import PharmaSerializer, UserSerializer

# Create your views here.
from .models import Pharma
from django.contrib.auth import authenticate

class LoginView(APIView):
    permission_classes = ()
    def post(self, request,):
        username = request.data.get("username")
        password = request.data.get("password")
        user = authenticate(username=username, password=password)
        if user:
            return Response({"token": user.auth_token.key})
        else:
            return Response({"error": "Wrong Credentials"}, status=status.HTTP_400_BAD_REQUEST)




class PharmaViewSet(viewsets.ModelViewSet):
    queryset = Pharma.objects.all()
    serializer_class = PharmaSerializer
    

class UserCreate(generics.CreateAPIView):
    authentication_classes = ()
    permission_classes = ()
    serializer_class = UserSerializer
