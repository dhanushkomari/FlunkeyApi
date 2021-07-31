from django.contrib import admin
from .models import Bot, Table, Delivery, DeliveryFinal

# Register your models here.

class BotAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['bot_no', 'name', 'color', 'status', 'avialable', 'ip', 'port']
admin.site.register(Bot, BotAdmin)


class TableAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['table_number', 'avialable']
admin.site.register(Table, TableAdmin)


class DeliveryAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['bot_no', 'bot_name', 'table_no']
admin.site.register(Delivery, DeliveryAdmin)

class DeliveryFinalAdmin(admin.ModelAdmin):
    list_per_page = 20
    list_display = ['bot_no', 'bot_name', 'table_no']
admin.site.register(DeliveryFinal, DeliveryFinalAdmin)