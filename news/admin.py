from models import Entry
from django.contrib import admin
from incunafein.admin import editor

class EntryOptions(editor.ItemEditor, admin.ModelAdmin):
    prepopulated_fields = {'slug': ('headline',)}
    list_display = ('__unicode__','pub_date',)
    show_on_top = ('headline', 'pub_date')
    raw_id_fields = []

admin.site.register(Entry, EntryOptions)
