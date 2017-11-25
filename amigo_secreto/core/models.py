# -*- coding: utf-8 -*-

from django.db.models import Model
from django.db.models import CharField
from django.db.models import BooleanField


class Participant(Model):
    name = CharField(
        primary_key=True,
        max_length=128,
        verbose_name='nome',
        blank=False,

    )
    chosen = BooleanField(
        blank=False,
        null=False,
        verbose_name=u'escolhido',
        default=False,
    )
    raffled = BooleanField(
        blank=False,
        null=False,
        verbose_name=u'sorteou',
        default=False,
    )

    def __repr__(self):
        return "<Participant <name={!r}, chosen={!r}, raffled={!r}>>".format(
            self.name, self.chosen, self.raffled)

    class Meta:
        verbose_name = "Participante"
        verbose_name_plural = "Participantes"
