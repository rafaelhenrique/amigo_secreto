# -*- coding: utf-8 -*-
import random

from amigo_secreto.core.models import Participant


def raffle_secret_friend(participant):
    """
    Raffle secret friend for an participant.

    Paramethers:
        participant (core.models.Participant): An participant object

    Return:
        an core.models.Participant object with secret friend
    """

    first_option_to_chose = Participant.objects.filter(
        chosen=False,
        raffled=False,
    ).exclude(name=participant.name)

    second_option_to_chose = Participant.objects.filter(
        chosen=False,
    ).exclude(name=participant.name)

    if not first_option_to_chose and not second_option_to_chose:
        raise Exception('Exception: {!r}'.format(participant))

    list_to_chose = first_option_to_chose or second_option_to_chose
    secret_friend = random.choice(list_to_chose)
    secret_friend.chosen = True
    participant.raffled = True
    secret_friend.save()
    participant.save()
    return secret_friend
