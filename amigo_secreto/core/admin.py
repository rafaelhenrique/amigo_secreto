# -*- coding: utf-8 -*-

from django.contrib import admin

from amigo_secreto.core.models import Member


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = ['name', 'chosen', 'raffled']
    fields = ['name', 'chosen', 'raffled']
