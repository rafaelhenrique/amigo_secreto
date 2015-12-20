# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django.forms import ModelChoiceField

from amigo_secreto.core.models import Member


class ModelChoiceField(ModelChoiceField):
    def label_from_instance(self, obj):
        return obj.name


class RaffleForm(ModelForm):
    name = ModelChoiceField(
        label=u'Selecione seu nome:',
        required=True,
        queryset=Member.objects.filter(raffled=False),
        empty_label=u'--Selecione--',
        to_field_name="name"
    )

    class Meta:
        model = Member
        fields = ('name', )
