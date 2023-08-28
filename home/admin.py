from django.contrib import admin
from .models import Post


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'user', 'slug', 'modified']
    search_fields = ('title', 'slug')
    list_filter = ('modified',)
    prepopulated_fields = {'slug': ('title', )}
    raw_id_fields = ('user', )