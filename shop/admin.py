from django.contrib import admin
from .models import Product, Order, OrderItem

# Register your models here.

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'is_low_stock')
    list_filter = ('stock',)
    search_fields = ('name',)
    
    def is_low_stock(self, obj):
        return obj.stock < 10
    is_low_stock.boolean = True
    is_low_stock.short_description = 'Low Stock'

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total', 'paid', 'created_at')
    list_filter = ('paid', 'created_at')
    search_fields = ('id', 'user__username')
    readonly_fields = ('created_at',)
    
    fieldsets = (
        ('Order Info', {
            'fields': ('user', 'total', 'paid')
        }),
        ('Dates', {
            'fields': ('created_at',)
        }),
    )

admin.site.register(OrderItem)