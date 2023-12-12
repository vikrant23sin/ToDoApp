from django.contrib import admin
from django.http.request import HttpRequest
from myapp.models import *
from django.contrib import messages

# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    list_display = ('date', 'title', 'details')

    def active(self, obj):
        return obj.is_active==1
    active.boolean=True

    def make_active(modeadmin, request, queryset):
        queryset.update(is_active=1)
        messages.success(request, "selected record marked as active successfully")

    def make_inactive(modeladmin, request, queryset):
        queryset.update(is_active=0)
        messages.success(request, "selected record marked as inactive successfully")
    
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
    
    admin.site.add_action(make_active, "make active")
    admin.site.add_action(make_inactive, 'make inactive')

admin.site.register(ToDo, ToDoAdmin)

