# -*- coding: utf-8 -*-
from django.http import HttpResponse
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.shortcuts import render_to_response
from django.template import RequestContext
from src.projetos.models import Projeto

def homepage_ocorrencia(request):
    values = RequestContext(request)
    return render_to_response('index_ocorrencia.html', values)

def cadastrar_ocorrencia(request, ocorrencia):
    return ocorrencia