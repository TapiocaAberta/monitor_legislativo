# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render_to_response
from django.template import RequestContext
from src.projetos.models import Projeto

def homepage_projetos(request):
    projetos = Projeto.objects.all()
    paginator = Paginator(projetos, 25) # Mostra N projetos por página

    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # Se o page request (9999) está fora da lista, mostre a última página.
    try:
        projetos = paginator.page(page)
    except (EmptyPage, InvalidPage):
        projetos = paginator.page(paginator.num_pages)

    values = RequestContext(request)
    values["projetos"] = projetos

    return render_to_response('index_projeto.html', values)
