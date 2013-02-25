# -*- coding: utf-8 -*-
from django.db import models
from src.politicos.models import Politico

class Projeto(models.Model):
    politico = models.ForeignKey(Politico)
    nome = models.CharField((u'Nome'), max_length=1000)
    descricao = models.CharField((u'Descrição'), max_length=1000)
    data_criacao = models.DateTimeField((u'Criado em'), auto_now_add=True)

    def __unicode__(self):
        return self.nome