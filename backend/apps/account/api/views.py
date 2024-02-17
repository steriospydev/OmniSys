from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema

from .serializers import SignupSerializer, LoginSerializer


class SignupAPIView(APIView):
    """This api will handle signup"""
    @swagger_auto_schema(request_body=SignupSerializer)
    def post(self,request):
        serializer = SignupSerializer(data = request.data)
        if serializer.is_valid():
            """If the validation success, it will created a new user."""
            serializer.save()
            res = { 'status' : status.HTTP_201_CREATED }
            return Response(res, status = status.HTTP_201_CREATED)
        res = { 'status' : status.HTTP_400_BAD_REQUEST, 'data' : serializer.errors }
        return Response(res, status = status.HTTP_400_BAD_REQUEST)
    

class LoginAPIView(APIView):
    """This api will handle login and return token for authenticate user."""
    @swagger_auto_schema(request_body=LoginSerializer)
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            username = serializer.validated_data["username"]
            password = serializer.validated_data["password"]
            user = authenticate(request, username=username, password=password)
            if user is not None:
                """We are reterving the token for authenticated user."""
                token = Token.objects.get(user=user)
                response = {
                        "status": status.HTTP_200_OK,
                        "message": "success",
                        "data": {
                                "Token" : token.key
                                }
                        }
                return Response(response, status = status.HTTP_200_OK)
            else :
                response = {
                        "status": status.HTTP_401_UNAUTHORIZED,
                        "message": "Invalid Email or Password",
                        }
                return Response(response, status = status.HTTP_401_UNAUTHORIZED)
        response = {
                "status": status.HTTP_400_BAD_REQUEST,
                "message": "bad request",
                "data": serializer.errors
                }
        return Response(response, status = status.HTTP_400_BAD_REQUEST)
