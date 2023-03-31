from django.contrib import admin
from users.models import CustomUser

# Register your models here.
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('email','phone_number','is_active','is_staff','is_superuser',)
    search_fields = ('email','phone_number', )

admin.site.register(CustomUser,CustomUserAdmin)