from django.contrib import admin
from .models import News
from markdownx.admin import MarkdownxModelAdmin

admin.site.register(News, MarkdownxModelAdmin)
