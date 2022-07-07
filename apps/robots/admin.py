from django.contrib import admin
from apps.robots.forms import RobotForm

from .models import Robot

# Register your models here.


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    form = RobotForm
    readonly_fields = ('created_at', 'modified_at', 'energy')
