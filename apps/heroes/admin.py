from django.contrib import admin
from .models import *


@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name',)
