from django.contrib import admin
from .models import *


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    search_fields = ('name',)
    list_display = ('id', 'name',)

