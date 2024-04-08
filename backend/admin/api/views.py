from rest_framework import mixins, serializers
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.request import Request
from rest_framework.response import Response
from admin.api.serializers import InterfaceSerializer
from admin.models import Interface
from utils.cmn_class import CustomPageNumberPagination


class InterfaceViewSet(
    mixins.CreateModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
):
    queryset = Interface.objects.all()
    serializer_class = InterfaceSerializer
    pagination_class = CustomPageNumberPagination
    permission_classes = [IsAuthenticated]

    class ListRequestSerializer(serializers.Serializer):
        is_all_query = serializers.BooleanField(required=False, default=False)
        ids = serializers.ListField(child=serializers.CharField(), allow_empty=True, required=False)

        def validate(self, attrs):
            self.is_all_query = attrs.get('is_all_query')
            self.ids = attrs.get('ids')
            return attrs

    def list(self, request: Request, *args, **kwargs):
        # 检测参数合法
        r_serializer = self.ListRequestSerializer(data=request.query_params)
        r_serializer.is_valid(raise_exception=True)

        is_all_query = r_serializer.is_all_query
        ids = r_serializer.ids

        queryset = self.filter_queryset(self.get_queryset())
        if ids:
            queryset = queryset.filter(id__in=ids)

        if not is_all_query:
            page = self.paginate_queryset(queryset)
            if page is not None:
                serializer = self.get_serializer(page, many=True)

                return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)  # 返回序列化后的数据

    @action(detail=True, methods=["get"])
    def ids(self, request, *args, **kwargs):
        return Response('usernames')
