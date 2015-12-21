# -*- coding: utf-8 -*-
import random

from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import View

from amigo_secreto.core.forms import RaffleForm
from amigo_secreto.core.models import Member


class Raffle(View):
    template_name = 'raffle.html'
    context = {}

    def get(self, request, *args, **kwargs):
        members = Member.objects.filter(chosen=False)
        if members:
            self.context['form'] = RaffleForm()
        else:
            self.context['form'] = None

        self.context['friend'] = None
        self.context['participant'] = None
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
            list_to_chose = Member.objects.filter(
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
