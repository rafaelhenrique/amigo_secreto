# -*- coding: utf-8 -*-
import random

from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import View
from django.utils import timezone

from amigo_secreto.core.forms import RaffleForm
from amigo_secreto.core.models import Participant


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
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))

    def post(self, request, *args, **kwargs):
        raffle_form = RaffleForm(request.POST)
        friend = None
        participant = None
        if raffle_form.is_valid():
            participant = raffle_form.cleaned_data.get('name')
            if participant.raffled:
                render_to_response(self.template_name,
                                   self.context, RequestContext(request))
            list_to_chose = Participant.objects.filter(
                chosen=False).exclude(name=participant.name)
            friend = random.choice(list_to_chose)
            friend.chosen = True
            participant.raffled = True
            friend.save()
            participant.save()

        self.context['form'] = raffle_form
        self.context['friend'] = friend
        self.context['participant'] = participant
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))
