from django.contrib import admin
from .models import Post, PostImage
from .forms import PostAdminForm



class PostImageInline(admin.TabularInline):
    model = PostImage
    extra = 0
    max_num = 10

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm 
    list_display = ['id','title', 'user', 'user_phone', 'category','province','price', 'is_approved']
    list_filter = ['is_approved', 'category']
    readonly_fields = ['user_phone']
    actions = ['approve_selected']
    inlines = [PostImageInline]

    fieldsets = (
        (None, {
            'fields': ('user', 'user_phone', 'category', 'title', 'description', 'price','province' ,'is_approved')
        }),
    )

    def user_phone(self, obj):
        return obj.user.phone if obj.user else '-'
    user_phone.short_description = "phone"

    def approve_selected(self, request, queryset):
        queryset.update(is_approved=True)
    approve_selected.short_description = "تایید آگهی‌های انتخاب شده"





admin.site.register(PostImage)