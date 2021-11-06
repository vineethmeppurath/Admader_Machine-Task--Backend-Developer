from django.contrib import admin

# Register your models here.
from core.models import TagModel, SnippetModel

admin.site.register(TagModel)
admin.site.register(SnippetModel)