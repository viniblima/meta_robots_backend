from django.contrib import admin
from .forms import RobotForm

from .models import Robot


@admin.register(Robot)
class RobotAdmin(admin.ModelAdmin):
    form = RobotForm
    readonly_fields = ('created_at', 'modified_at', 'energy')
