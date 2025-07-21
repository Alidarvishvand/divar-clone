from django.contrib import admin
from .models import Report,AdminSupportMessage,AdminActionLog,SystemConfig

@admin.register(Report)
class ReportAdmin(admin.ModelAdmin):
    list_display = ('id', 'reporter', 'report_type', 'reported_user', 'reported_post', 'is_resolved', 'created_at')
    list_filter = ('report_type', 'is_resolved', 'created_at')
    search_fields = ('reporter__email', 'reported_user__email', 'message', 'reason')
    readonly_fields = ('created_at',)

    fieldsets = (
        (None, {
            'fields': ('reporter', 'report_type', 'reported_user', 'reported_post', 'message', 'reason', 'is_resolved')
        }),
        ('Timestamps', {
            'fields': ('created_at',),
        }),
    )


@admin.register(AdminSupportMessage)
class AdminSupportMessageAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'subject', 'is_answered', 'created_at')
    list_filter = ('is_answered', 'created_at')
    search_fields = ('user__email', 'subject', 'message')
    readonly_fields = ('created_at',)
    
    


@admin.register(SystemConfig)
class SystemConfigAdmin(admin.ModelAdmin):
    list_display = ('id', 'key', 'value', 'updated_at')
    search_fields = ('key', 'value')
    readonly_fields = ('updated_at',)



@admin.register(AdminActionLog)
class AdminActionLogAdmin(admin.ModelAdmin):
    list_display = ('id', 'admin_user', 'action', 'target_model', 'target_id', 'created_at')
    list_filter = ('target_model', 'admin_user')
    search_fields = ('admin_user__email', 'action', 'target_model')
    readonly_fields = ('created_at',)