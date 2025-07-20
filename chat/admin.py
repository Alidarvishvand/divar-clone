from django.contrib import admin
from .models import ChatMessage

class ReplyInline(admin.StackedInline):
    model = ChatMessage
    fk_name = 'parent'
    extra = 1
    fields = ['sender', 'receiver', 'message']
    readonly_fields = []
    verbose_name = "پاسخ"
    verbose_name_plural = "پاسخ‌ها"

    def save_new_objects(self, formset, commit=True):
        objs = super().save_new_objects(formset, commit=False)
        parent_obj = formset.instance  
        for obj in objs:
            obj.post = parent_obj.post  
            if commit:
                obj.save()
        return objs


@admin.register(ChatMessage)
class ChatMessageAdmin(admin.ModelAdmin):
    list_display = ['id', 'post', 'sender', 'receiver', 'short_message', 'timestamp']
    list_filter = ['post', 'sender', 'receiver']
    search_fields = ['message', 'sender__username', 'receiver__username']
    readonly_fields = ['timestamp']
    inlines = [ReplyInline]  

    def short_message(self, obj):
        return obj.message[:40]
