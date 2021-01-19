from rest_framework.pagination import PageNumberPagination
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.pagination import CursorPagination


# 基础分页器
class MyPageNumberPagination(PageNumberPagination):
    # 指定每页分页的数量
    page_size = 3
    # 指定获取第几页的对象
    page_query_param = "page"
    # 指定前端修改每页分页数量的key
    page_size_query_param = "page_size"
    # 指定前端可以获取的每页的最大数量
    max_page_size = 5


class MyLimitOffsetPagination(LimitOffsetPagination):
    # 默认获取的每页分页的数量
    default_limit = 2
    # 指定前端修改每页展示对象的key
    limit_query_param = "limit"
    # 指定前端偏移数量的key
    offset_query_param = "offset"
    # 每页获取的最大数量
    max_limit = 5


# 游标分页器 （对页码进行了加密）
class MyCursorPagination(CursorPagination):
    page_size = 3
    cursor_query_param = "cursor"
    max_page_size = 5
    ordering = "-price"
