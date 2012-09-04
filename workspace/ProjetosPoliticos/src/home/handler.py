#-*- coding: utf-8 -*-
'''
Created on 13/08/2012

@author: PauloLuan
'''
from zen.ce import cengine

class home():
    def index(self):
        values = {"projetos_link": "/projetos", #cengine.handler_to_path(home.index 
                  "politicos_link": "/politicos", 
                  "mapa_link": "/mapa",
                  "sobre_link": "/sobre"}
        self.write_template("home.html", values)

    def sobre(self):
        values = {"projetos_link": "/projetos", #cengine.handler_to_path(home.index 
                  "politicos_link": "/politicos", 
                  "mapa_link": "/mapa",
                  "sobre_link": "/sobre"}
        self.write_template("about.html", values)
