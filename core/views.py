from rest_framework import viewsets, status
from rest_framework.response import Response
from .serializer import MyDataExcelSerializer
from rest_framework_bulk import BulkModelViewSet, BulkCreateModelMixin
from .models import MyDataExcel
import pandas as pd


class MyDataExcelViewSet(BulkModelViewSet):

    queryset = MyDataExcel.objects.all()
    serializer_class = MyDataExcelSerializer

    def get_queryset(self):
        return self.queryset

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        list_data = []
        try:
            excel_file = request.data['file']
            read_file = pd.read_excel(excel_file)
            for i in read_file.itertuples(index=False):
                list_data.append({'field_1': str(i[0])})
        except Exception as e:
            print(e)
        del request.data['file']
        bulk = isinstance(list_data, list)

        if not bulk:
            return super(BulkCreateModelMixin, self).create(request, *args, **kwargs)

        else:
            serializer = self.get_serializer(data=list_data, many=True)
            serializer.is_valid(raise_exception=True)
            self.perform_bulk_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def perform_bulk_create(self, serializer):
        return self.perform_create(serializer)
