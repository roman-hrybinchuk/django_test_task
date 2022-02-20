from django.contrib import admin
from .models import Worker, TradePoint, Visit


# Register your models here.

@admin.register(Worker)
class WorkerAdmin(admin.ModelAdmin):
    search_fields = ['name', 'phone_number']
    list_display = ['name', 'phone_number']


@admin.register(TradePoint)
class TradePointAdmin(admin.ModelAdmin):
    search_fields = ['name', ]
    list_display = ['name', 'worker']


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    list_display = ['trade_point', 'timestamp', 'latitude', 'longitude']
