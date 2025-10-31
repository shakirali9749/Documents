from django.contrib import admin

from .models import Payment

@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('transaction_id','booking','status','amount','payment_method','created_at')
    search_fields = ('transaction_id','booking_customer_username')
    list_filter = ('status','payment_method')