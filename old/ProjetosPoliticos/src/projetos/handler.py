#-*- coding: utf-8 -*-
'''
Created on 13/08/2012

@author: PauloLuan
'''
from __future__ import unicode_literals
from google.appengine.api import users
from projetos.model import Projeto
from zen.ce import cengine

class home():
    def index(self):
        projetos = Projeto.find_all()
        values = {"aba_ativa": "projetos",
                  "projetos": projetos,
                  "like_url": cengine.to_path(home.like_project),
                  "dislike_url": cengine.to_path(home.dislike_project)
        }
        self.write_template("projetos.html", values)

    def detalhe(self, key_projeto):
        projeto = Projeto.find_by_id(key_projeto)
        values = {
            "aba_ativa": "projetos",
            "projeto": projeto
        }
        self.write_template("detalhe_projeto.html", values)

    def like_project(self, key_projeto):
        Projeto.like(key_projeto)
        self.redirect("/projetos")

    #TODO: criar decorator para verificar se o usuário já votou
    #@usuario já votou
    def dislike_project(self, key_projeto):
        Projeto.dislike(key_projeto)
        self.redirect("/projetos")

class edit():
    def index(self):
        projetos = Projeto.find_all()
        values = {"aba_ativa": "projetos",
                  "projetos": projetos,
                  "like_url": cengine.to_path(home.like_project),
                  "dislike_url": cengine.to_path(home.dislike_project)
        }
        self.write_template("list_edit_projetos.html", values)

    def delete(self, id_projeto):
        Projeto.delete(id_projeto)
        self.redirect(cengine.to_path(edit.index))

    def edit_projeto(self, key_projeto):
        projeto = Projeto.find_by_id(key_projeto)
        values = {"aba_ativa": "projetos",
                  "projeto": projeto,
                  "save_url": cengine.to_path(edit.save_edit)
        }
        self.write_template("edit_projeto.html", values)

    def save_edit(self):
        key = self.get("key_projeto")
        projeto = Projeto.find_by_id(key)

        projeto.nome = self.get("nome")
        projeto.link = self.get("link")
        projeto.descricao = self.get("descricao")

        projeto.put()
        self.redirect(cengine.to_path(edit.index))

    def new(self):
        values = {"aba_ativa": "projeto",
                  "save_url": cengine.to_path(edit.save_new)
        }
        self.write_template("create_projeto.html", values)

    def save_new(self):
        projeto = Projeto(
            nome=self.get("nome"),
            link=self.get("link"),
            descricao=self.get("descricao"),
            nota=0,
            likes=0,
            dislikes=0
        )
        projeto.put()
        self.redirect(cengine.to_path(edit.index))
