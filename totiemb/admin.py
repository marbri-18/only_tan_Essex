from django.contrib import admin
from .models import Product
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):

    summernote_fields = ('description')

# Register your models here.

