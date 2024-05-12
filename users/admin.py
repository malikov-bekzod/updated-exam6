from django.contrib import admin
from .models import User
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(User)
class UserAdmin(ImportExportModelAdmin):
    list_display = ["first_name", "last_name", "email", "username"]
    list_display_links = ["first_name", "last_name", "email", "username"]
    search_fields = ["first_name", "last_name", "email", "username"]
    ordering = ["first_name"]
