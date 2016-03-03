from django.contrib import admin
from models import HS300Const, ZZ500Const


class HS300ConstAdmin(admin.ModelAdmin):
    fields = ['flashTime', 'date', 'code', 'weight']
    list_display = ['flashTime', 'date', 'code', 'weight']
admin.site.register(HS300Const, HS300ConstAdmin)


class ZZ500ConstAdmin(admin.ModelAdmin):
    fields = ['flashTime', 'date', 'code', 'weight']
    list_display = ['flashTime', 'date', 'code', 'weight']
admin.site.register(ZZ500Const, ZZ500ConstAdmin)
