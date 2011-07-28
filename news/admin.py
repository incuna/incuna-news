from models import Entry, NewsCategory
from django.contrib import admin
from incunafein.admin import editor

class EntryOptions(editor.ItemEditor, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('headline',)}
    list_display = ('__unicode__','pub_date',)
    show_on_top = ('headline', 'pub_date')
    raw_id_fields = []

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}
    
admin.site.register(Entry, EntryOptions)
admin.site.register(NewsCategory, CategoryAdmin)
