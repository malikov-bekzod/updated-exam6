from django.contrib import admin
from .models import Review, Testimonial 
from import_export.admin import ImportExportModelAdmin
# Register your models here.


@admin.register(Review)
class ReviewAdmin(ImportExportModelAdmin):
    list_display = ["product", "user", "text","rate","created_date"]
    list_display_links = ["product", "user", "text", "rate", "created_date"]
    search_fields = ["text","user"]

@admin.register(Testimonial)
class TestimonialAdmin(ImportExportModelAdmin):
    list_display = ["text","first_name","last_name","profession"]