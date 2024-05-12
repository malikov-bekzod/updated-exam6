from django.contrib import admin
from .models import Country,Category,Product,Cart,Product_category
from import_export.admin import ImportExportModelAdmin

# Register your models here.


@admin.register(Country)
class CountryAdmin(ImportExportModelAdmin):
    list_display = ["name",]
    list_display_links = ["name",]
    search_fields = ["name",]
    ordering = ["name"]


@admin.register(Category)
class CategoryAdmin(ImportExportModelAdmin):
    list_display = ["name","product_count"]
    list_display_links = ["name", "product_count"]
    search_fields = ["name", "product_count"]
    ordering = ["name"]


@admin.register(Product)
class ProductAdmin(ImportExportModelAdmin):
    list_display = ["name", "description","old_price","new_price","quantity","rating","origin_country"]
    list_display_links = [
        "name",
        "description",
        "old_price",
        "new_price",
        "quantity",
        "rating",
        "origin_country",
    ]
    search_fields = ["name"]
    ordering = ["name"]


@admin.register(Cart)
class CartAdmin(ImportExportModelAdmin):
    list_display = ["user", "product","created_date"]
    list_display_links = ["user", "product", "created_date"]
    search_fields = ["user", "product"]
    ordering = [ "product",]


@admin.register(Product_category)
class Product_categoryAdmin(ImportExportModelAdmin):
    list_display = [ "product", "category"]
    list_display_links = ["product", "category"]
    search_fields = ["product", "category"]
    ordering = [
        "product",
    ]
