# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from models import Politico
from src.projetos.models import Projeto

def homepage_politico(request):
    politicos = Politico.objects.all().order_by("nome")
    values = RequestContext(request)
    values['politicos'] = politicos
    return render_to_response('index_politico.html', values)

def perfil_politico(request, politico_id):
    politico = Politico.objects.get(id=politico_id)
    projetos = Projeto.objects.filter(politico=politico)
    values = RequestContext(request)
    values["politico"] = politico
    values["projetos"] = projetos
    return render_to_response('perfil_politico.html', values)