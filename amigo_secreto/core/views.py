# -*- coding: utf-8 -*-

from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.views.generic import View

from amigo_secreto.core.forms import RaffleForm


class Raffle(View):
    template_name = 'raffle.html'
    context = {}

    def get(self, request, *args, **kwargs):
        self.context['form'] = RaffleForm()
        return render_to_response(self.template_name,
                                  self.context, RequestContext(request))

    # def post(self, request, *args, **kwargs):
    #     search_form = SearchPartnerFactor(request.POST)
    #     if search_form.is_valid():
    #         factors = PartnerFactor.get_factors(**search_form.cleaned_data)
    #     else:
    #         factors = PartnerFactor.objects.filter(status=True).order_by("-id")

    #     factors = create_paginator(factors, request, page_results=10)
    #     self.context['factors'] = factors
    #     self.context['form'] = search_form
    #     return render_to_response(self.template_name,
    #                               self.context, RequestContext(request))