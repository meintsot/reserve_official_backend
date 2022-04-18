from django.contrib import admin
from .models import Company, Schedule, Notification


admin.site.register(Company)
admin.site.register(Schedule)
admin.site.register(Notification)
