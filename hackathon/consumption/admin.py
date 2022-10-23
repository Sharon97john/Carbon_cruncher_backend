from django.contrib import admin

# Register your models here.
from .models import device_smart, user_table, consumption_calc, treek

admin.site.register(device_smart)
admin.site.register(user_table)
admin.site.register(consumption_calc)
admin.site.register(treek)