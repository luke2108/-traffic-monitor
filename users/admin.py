from django.contrib import admin

from .models import UserError


class UserMonitorAdmin(admin.ModelAdmin):
    list_display = ["ip_user", "user_agent", "domain", "status", "timestamp"]
    search_fields = ["ip_user"]

admin.site.register(UserError, UserMonitorAdmin)