# -*- coding: utf-8 -*-

from django.forms import Form
from django.forms import CharField


class RaffleForm(Form):
    participant_name = CharField(
        label=u'Seu nome é:',
        required=True,
    )
