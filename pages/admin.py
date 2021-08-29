from django.contrib import admin

# Register your models here.

from .models import Pages


class PagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')  # this is to show what will display
    list_display_links = ('id', 'title')
    list_filter = ('title',)
    list_editable = ('is_published',)
    search_fields = ('title', 'description', 'city', 'state', 'phone')
    list_per_page = 25


admin.site.register(Pages, PagesAdmin)  # it is necessary to call PagesAdmin
