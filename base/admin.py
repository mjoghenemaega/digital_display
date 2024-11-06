# admin.py
from django.contrib import admin
from .models import News

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'view_count', 'created_at')
    list_filter = ('category',)
    search_fields = ('title',)
