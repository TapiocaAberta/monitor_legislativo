# -*- coding: utf-8 -*-
from django.db import models

class Ocorrencia(models.Model):
    nome = models.CharField((u'Nome'), max_length=1000)
    descricao = models.CharField((u'Descrição'), max_length=1000)
    data_criacao = models.DateTimeField((u'Criado em'), auto_now_add=True)

    def __unicode__(self):
        return self.nome