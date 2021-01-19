from django_filters.rest_framework import FilterSet

from drfapp.models import Computer


class ComputerFilterSet(FilterSet):
    from django_filters import filters
    min_price = filters.NumberFilter(field_name="price", lookup_expr="gte")
    max_price = filters.NumberFilter(field_name="price", lookup_expr="lte")

    class Meta:
        # 为哪个模型定义的过滤类
        model = Computer
        fields = ['min_price', "max_price", "brand", "name"]
