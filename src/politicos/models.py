# -*- coding: utf-8 -*-
from django.db import models

class Politico(models.Model):
    nome = models.CharField((u'Nome'), max_length=100)
    descricao = models.CharField((u'Descrição'), max_length=1000)
    email = models.EmailField((u'Email'), unique=True)
    telefone = models.CharField((u'Telefone'), max_length=20, blank=True)
    data_criacao = models.DateTimeField((u'Criado em'), auto_now_add=True)

    def __unicode__(self):
        return self.nome

