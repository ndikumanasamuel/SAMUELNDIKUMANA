from django.contrib import admin
from .models import Words


class WordsAdmin(admin.ModelAdmin):
    list_display = ('name', 'description',)


admin.site.register(Words, WordsAdmin)
