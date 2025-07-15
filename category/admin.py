from django.contrib import admin
from mptt.admin import DraggableMPTTAdmin
from .models import Category


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin):
    mptt_indent_field = "name"
    list_display = (
        "id",
        "tree_actions",
        "indented_title",
        "slug",
        "parent",
    )
    list_display_links = ("indented_title",)
    prepopulated_fields = {"slug": ("name",)}
    ordering = ["id"]
