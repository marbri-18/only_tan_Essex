from django.contrib import admin
from .models import Product, Customer, Session
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Product)
class ProductAdmin(SummernoteModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('maker', 'created_on')
    list_display = ('title', 'maker', 'created_on')
    search_fields = ('title', 'description')
    summernote_fields = ('description')

@admin.register(Customer)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('lname', 'fname', 'username', 'dob', 'created_on')
    list_filter = ('created_on', 'is_admin')
    search_fields = ('lname', 'username', 'date_of_birth')

@admin.register(Session)
class SessionAdmin(admin.ModelAdmin):
    list_display = ('session_date_time', 'customer_name', 'over_18_yrs', 'tandc_understood')
    list_filter = ('session_date_time', 'customer_name')






