from django.db import models

class UpperCaseCharField(models.CharField):
    """Custom field lưu text tự động viết hoa"""
    def get_prep_value(self, value):
        return str(value).upper() if value else value

class Category(models.Model):
    code = UpperCaseCharField(max_length=10, unique=True)
    description = models.CharField(max_length=200)
