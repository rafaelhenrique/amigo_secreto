# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.views.generic import View
from django.utils import timezone

from amigo_secreto.core.forms import RaffleForm
from amigo_secreto.core.models import Participant
from amigo_secreto.core.use_cases import raffle_secret_friend


class Raffle(View):
    template_name = 'raffle.html'
    context = {}

    def get(self, request, *args, **kwargs):
        members = Participant.objects.filter(chosen=False)
        if members:
            self.context['form'] = RaffleForm()
        else:
            self.context['form'] = None

        self.context['friend'] = None
        self.context['participant'] = None
        self.context['year'] = timezone.now().year
        return render(request, self.template_name, self.context)

    def post(self, request, *args, **kwargs):
        raffle_form = RaffleForm(request.POST)
        friend = None
        participant = None
        if raffle_form.is_valid():
            participant = raffle_form.cleaned_data.get('name')
            friend = raffle_secret_friend(participant)

        self.context['form'] = raffle_form
        self.context['friend'] = friend
        self.context['participant'] = participant
        return render(request, self.template_name, self.context)
