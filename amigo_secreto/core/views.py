# -*- coding: utf-8 -*-
import random

from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import View
from django.http import JsonResponse

from amigo_secreto.core.forms import RaffleForm
from amigo_secreto.core.models import Member


class Raffle(View):
    template_name = 'raffle.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = RaffleForm()
        self.context['friend'] = None
        self.context['participant'] = None
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))

    def post(self, request, *args, **kwargs):
        raffle_form = RaffleForm(request.POST)
        friend = None
        if raffle_form.is_valid():
            participant = raffle_form.cleaned_data.get('name')
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


class List(View):
    def get(self, request, *args, **kwargs):
        return JsonResponse({'participants': Member.objects.all()})
