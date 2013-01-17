#-*- coding: utf-8 -*-
'''
Created on 13/08/2012

@author: PauloLuan
'''
from __future__ import unicode_literals
from google.appengine.api import users
from usuario.model import User
from zen.ce import cengine, cehandler

class home():
    def index(self):
        self.write_template("login.html")

    def formulario(self):
        if User.current_user():
            self.redirect("/")
        else:
            url = cengine.to_path(home.salvar)
            values = {"salvar_url":url}
            self.write_template("user_form.html", values)
        
    def salvar(self):
        google_user = users.get_current_user()
        id = google_user.user_id()
        email = google_user.email()
        u = User(
                 id=id,
                 nome=self.get("nome"),
                 sobrenome=self.get("sobrenome"),
                 email=email
        )
        u.put()
        self.redirect("/")
        
