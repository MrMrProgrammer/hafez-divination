from django.contrib import admin

from .models import Poem

from unfold.admin import ModelAdmin


@admin.register(Poem)
class PoemAdmin(ModelAdmin):
    list_display = ['poem_detail','number', 'poem', 'interpretation', 'is_active', 'created_at_shamsi', 'updated_at_shamsi']
    search_fields = ['number', 'poem', 'interpretation']
    list_filter = ['is_active',]
    readonly_fields = ['created_at_shamsi', 'updated_at_shamsi']
    ordering = ['number']
    list_per_page = 20
