# -*- coding: utf-8 -*-

from django.db.models import Model
from django.db.models import CharField
from django.db.models import BooleanField


class Member(Model):
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
        return "Member({!r}, {!r}, {!r})".format(
            self.name, self.chosen, self.raffled)
