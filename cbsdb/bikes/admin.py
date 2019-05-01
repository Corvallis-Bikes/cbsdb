from django.contrib import admin
from .models import Bike,People,Sale,ShiftLog,UseLog

admin.site.register(Bike)
admin.site.register(People)
admin.site.register(Sale)
admin.site.register(ShiftLog)
admin.site.register(UseLog)

# Register your models here.
