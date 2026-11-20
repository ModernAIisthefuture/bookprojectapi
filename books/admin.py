
from django.contrib import admin

from .models import APIClient, Book


@admin.register(APIClient)
class APIClientAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'name',
        'api_key',
        'is_active',
        'created_at'
    )

    list_filter = ('is_active',)

    search_fields = ('name',)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'author',
        'price',
        'published_date'
    )

    search_fields = ('title', 'author')
