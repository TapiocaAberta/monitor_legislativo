#-*- coding: utf-8 -*-
'''
Created on 13/08/2012

@author: PauloLuan
'''
from __future__ import unicode_literals
from google.appengine.ext import ndb
import logging

class Projeto(ndb.Model):
    nome = ndb.StringProperty(required=False)
    nota = ndb.IntegerProperty(required=False, default=0)
    likes = ndb.IntegerProperty(required=False, default=0)
    dislikes = ndb.IntegerProperty(required=False, default=0)
    likes_computed = ndb.IntegerProperty(required=False, default=0)
    dislikes_computed = ndb.IntegerProperty(required=False, default=0)
    link = ndb.StringProperty(required=False)
    descricao = ndb.TextProperty(required=False)

    @classmethod
    def find_by_id(cls, key_projeto):
        projeto_key = ndb.Key(urlsafe=key_projeto)
        projeto = projeto_key.get()
        return projeto

    @classmethod
    def like(cls, key_projeto):
        projeto_key = ndb.Key(urlsafe=key_projeto)
        projeto = projeto_key.get()
        current_likes = int(projeto.likes)
        projeto.likes = current_likes + 1

        likes = float(projeto.likes)
        dislikes = float(projeto.dislikes)
        projeto.likes_computed = int((likes / (likes + dislikes)) * 100)
        projeto.dislikes_computed = int((dislikes / (likes + dislikes)) * 100)

        projeto.put()

    @classmethod
    def dislike(cls, key_projeto):
        projeto_key = ndb.Key(urlsafe=key_projeto)
        projeto = projeto_key.get()
        current_dislikes = int(projeto.dislikes)
        projeto.dislikes = current_dislikes + 1

        likes = float(projeto.likes)
        dislikes = float(projeto.dislikes)
        projeto.likes_computed = int((likes / (likes + dislikes)) * 100)
        projeto.dislikes_computed = int((dislikes / (likes + dislikes)) * 100)

        projeto.put()

    @classmethod
    def find_all(cls):
        projetos = Projeto.query().fetch(20)
        return projetos

    @classmethod
    def find_tree_projects(cls):
        projetos = Projeto.query().fetch(3)
        return projetos

    @classmethod
    def delete(self, id_projeto):
        projeto_id = int(id_projeto)
        key = ndb.Key(Projeto, projeto_id)
        key.delete()

