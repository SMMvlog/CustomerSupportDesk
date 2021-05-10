from django.contrib import admin
from .models import CustomerEnquiry
# Register your models here.

@admin.register(CustomerEnquiry)
class CustomerEnquiryAdmin(admin.ModelAdmin):
    list_display = ['id','name', 'mobile','email','queries']

