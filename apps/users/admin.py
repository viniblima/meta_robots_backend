from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User
from .forms import UserChangeForm, UserCreationForm

# Register your models here.


@admin.register(User)
class userAdmin(BaseUserAdmin):
    form = UserChangeForm
    add_form = UserCreationForm
    list_display = ('name', 'email', 'is_active',)
    list_filter = ('name', 'email', 'is_active',)
    list_display_links = ('name', 'email',)
    readonly_fields = ('created_at', 'updated_at', 'is_staff',
                       'is_superuser', 'last_login',)

    fieldsets = (
        ('Dados principais',
         {'fields': ('name', 'email', 'password',)},),
        ('Informações pessoais: ',
         {'fields': ('gender', 'date_of_birth', 'is_confirm')}),
        ('Permissões', {'fields': ('is_staff',
                                   'is_superuser',), },),
        ('Datas importantes',
         {'fields': ('created_at', 'updated_at', 'last_login',)}
         )
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2',),
        }),
    )

    search_fields = ('email', 'name',)
    ordering = ('email', 'name', )
