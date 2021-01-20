from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication

from api.authentication import MyAuthentication
from api.serializer import UserModelSerializer


class UserDetailAPIVIew(APIView):
    #只允许登录以后的用户访问

    permission_classes = [IsAuthenticated]
    # 通过jwt的认证类来为访问当前接口的请求进行认证
    authentication_classes = [MyAuthentication]

    def get(self, request, *args, **kwargs):
        return Response({"username": request.user.username})


class LoginAPIView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        # 账号使用account接收 密码使用pwd

        serializer = UserModelSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        return Response({
            "user": UserModelSerializer(serializer.obj).data,
            "token": serializer.token
        })
