from .serializers import FreelancerSignUpSerializer,ClientSignUpSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token



class FreelancerSignUpView(generics.CreateAPIView):
    serializer_class = FreelancerSignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "Freelancer account created successfully",
        })

class ClientSignUpView(generics.CreateAPIView):
    serializer_class = ClientSignUpSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": Token.objects.get(user=user).key,
            "message": "Freelancer account created successfully",
        })