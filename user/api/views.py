from .serializers import UserSerializer,FreelancerSignUpSerializer,ClientSignUpSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework import status
from rest_framework.views import APIView
from .permissions import IsClientUser,IsFreelanceUser
from rest_framework import permissions



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


class CustomObtainToken(ObtainAuthToken):
    def post(self,request,*args, **kwargs):
        serializer = self.serializer_class(data=request.data,context={'request':request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token,created = Token.objects.get_or_create(user=user)
        return Response({
            'token':token.key,
            'user_id':user.pk,
            'is_client':user.is_client,
            'email':user.email,
        }
        )


class LogoutView(APIView):
    def post(self, request,format=None):
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class ClientOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsClientUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user

class FreelanceOnlyView(generics.RetrieveAPIView):
    permission_classes=[permissions.IsAuthenticated&IsFreelanceUser]
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user