
from django.contrib import admin
from .models import Advertisement, Category, Comment

@admin.register(Advertisement)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'user', 'category', 'price', 'is_active', 'created_at')
    list_filter = ('category', 'is_active')

admin.site.register(Category)
admin.site.register(Comment)

