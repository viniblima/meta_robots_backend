from django.contrib import admin
from .forms import TrainForm
from .models import Train


@admin.register(Train)
class TrainAdmin(admin.ModelAdmin):
    form = TrainForm
    readonly_fields = ('created_at', 'modified_at',
                       'robot', 'trained_attribute',)
