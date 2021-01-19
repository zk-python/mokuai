from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.pagination import PageNumberPagination

from drfapp.filter import ComputerFilterSet
from drfapp.models import Computer
from drfapp.pagination import MyPageNumberPagination, MyLimitOffsetPagination, MyCursorPagination
from drfapp.serializer import ComputerModelSerializer
from drfapp.throttle import MyThrottle


class UserAPIView(APIView):
    throttle_classes = [MyThrottle]

    def get(self, request, *args, **kwargs):
        return Response("OK")

    def post(self, request):
        return Response("写操作")


class ComputerAPIView(ListAPIView):
    queryset = Computer.objects.all()
    serializer_class = ComputerModelSerializer

    """
    http://127.0.0.1:8000/api/computers/?ordering=price&search=小米
    """

    # 通过此参数指定要使用的过滤类
    filter_backends = [DjangoFilterBackend, OrderingFilter]

    # 指定排序的条件
    ordering = ["price"]

    # 查询价格大于3000小于9000的电脑
    filter_class = ComputerFilterSet

    # 指定当前视图要使用的分页器
    pagination_class = MyPageNumberPagination
