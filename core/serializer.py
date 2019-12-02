from rest_framework.serializers import ModelSerializer
from rest_framework_bulk import BulkListSerializer, BulkSerializerMixin
from .models import MyDataExcel


class MyDataExcelSerializer(BulkSerializerMixin, ModelSerializer):

    class Meta:
        list_serializer_class = BulkListSerializer
        model = MyDataExcel
        fields = '__all__'
