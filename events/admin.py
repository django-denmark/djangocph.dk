from django.contrib import admin

from markdownx.admin import MarkdownxModelAdmin
from .models import Event


@admin.register(Event)
class EventAdmin(MarkdownxModelAdmin):
    pass

