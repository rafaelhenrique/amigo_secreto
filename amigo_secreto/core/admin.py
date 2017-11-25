# -*- coding: utf-8 -*-

from django.contrib import admin

from amigo_secreto.core.models import Participant


@admin.register(Participant)
class ParticipantAdmin(admin.ModelAdmin):
    list_display = ['name', 'chosen', 'raffled']
    fields = ['name', 'chosen', 'raffled']
