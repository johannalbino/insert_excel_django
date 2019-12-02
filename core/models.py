from django.db import models


class MyDataExcel(models.Model):
    field_1 = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return str(self.field_1)

    class Meta:
        db_table = 'my_data_excel'


class MyFileExcel(models.Model):
    file_1 = models.FileField(upload_to='upload/', blank=True, null=True)

    def __str__(self):
        return str(self.file_1)

    class Meta:
        db_table = 'my_file_excel'
