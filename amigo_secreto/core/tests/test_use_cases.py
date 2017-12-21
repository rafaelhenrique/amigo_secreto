# -*- coding: utf-8 -*-
from django.test import TestCase
from mixer.backend.django import mixer

from amigo_secreto.core.models import Participant
from amigo_secreto.core.use_cases import raffle_secret_friend


class UseCasesTest(TestCase):

    def test_raffle_secret_friend_with_pair_participants(self):
        mixer.cycle(50).blend('core.Participant')
        participants = Participant.objects.all()

        for _ in range(participants.count()):
            participant = Participant.objects.filter(raffled=False).first()
            raffle_secret_friend(participant)

        all_chosen = all(participants.values_list('chosen', flat=True))
        all_raffled = all(participants.values_list('raffled', flat=True))
        self.assertTrue(all_chosen)
        self.assertTrue(all_raffled)

    def test_raffle_secret_friend_with_unpair_participants(self):
        mixer.cycle(51).blend('core.Participant')
        participants = Participant.objects.all()

        for _ in range(participants.count()):
            participant = Participant.objects.filter(raffled=False).first()
            raffle_secret_friend(participant)

        all_chosen = all(participants.values_list('chosen', flat=True))
        all_raffled = all(participants.values_list('raffled', flat=True))
        self.assertTrue(all_chosen)
        self.assertTrue(all_raffled)

    def test_raffle_secret_friend_different_secret_friends_with_pair_participants(self):
        mixer.cycle(50).blend('core.Participant')
        participants = Participant.objects.all()

        secret_friends = []
        for _ in range(participants.count()):
            participant = Participant.objects.filter(raffled=False).first()
            secret_friend = raffle_secret_friend(participant)
            secret_friends.append(secret_friend.pk)

        for participant in participants:
            self.assertEqual(secret_friends.count(participant.pk), 1)

    def test_raffle_secret_friend_different_secret_friends_with_unpair_participants(self):
        mixer.cycle(51).blend('core.Participant')
        participants = Participant.objects.all()

        secret_friends = []
        for _ in range(participants.count()):
            participant = Participant.objects.filter(raffled=False).first()
            secret_friend = raffle_secret_friend(participant)
            secret_friends.append(secret_friend.pk)

        for participant in participants:
            self.assertEqual(secret_friends.count(participant.pk), 1)
