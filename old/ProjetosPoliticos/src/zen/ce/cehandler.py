'''
Created on 02/02/2011

@author: Renzo Nuccitelli
'''

import webapp2
from zen.ce import cengine
from common import tmpl
from google.appengine.api import users
from usuario.model import User


class BaseHandler(webapp2.RequestHandler):
    def get(self):
        self.make_convetion()
        
    def post(self):
        self.make_convetion()
        
    def make_convetion(self):
        (handler_class, method_name, params) = cengine.to_handler(self.request.path)
        handler = handler_class()
        handler.request = self.request
        handler.get = self.request.get
        handler.write = self.response.out.write
        handler.response = self.response
        handler.handler = self
        handler.redirect = self.redirect
        handler.render = tmpl.render
        
        def write_template(template_name, values={}):
            user = User.current_user()
            url = None
            logout = None
            if user:
                logout = users.create_logout_url("/")
            else:
                url = users.create_login_url("/usuario/formulario")
            
            values_locals = {
                "current_user":user,
                "logout_url": logout,
                "login_url":url,
                "projetos_link": "/projetos", #cengine.to_path(projeto.index) 
                "politicos_link": "/politicos",
                "mapa_link": "/mapa",
                "sobre_link": "/",
            }
            values.update(values_locals)
            # concatena o dicionário do parâmetro com os dos valores presentes nesta função.
            
            handler.write(tmpl.render(template_name, values))
            
        handler.write_template = write_template
        method = getattr(handler, method_name)
        method(*params)


app = webapp2.WSGIApplication([("/.*", BaseHandler)], debug=False)

