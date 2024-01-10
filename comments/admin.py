from django.contrib import admin
from comments.models import Comment

@admin.register(Comment)
class CommnetAdmin(admin.ModelAdmin):
    list_display = ['content','created_at', 'user', 'post']