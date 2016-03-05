from django.contrib import admin
from models import Index, IndexConst


class IndexAdmin(admin.ModelAdmin):
    fields = ['name', 'loadUrl']
    list_display = ['name', 'loadUrl']
admin.site.register(Index, IndexAdmin)


class IndexConstAdmin(admin.ModelAdmin):
    fields = ['index', 'date', 'code', 'weight', 'flashTime']
    list_display = ['index', 'date', 'code', 'weight', 'flashTime']
    list_filter = ['index', 'date']
admin.site.register(IndexConst, IndexConstAdmin)
