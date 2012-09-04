#-*- coding: utf-8 -*-
'''
Created on 13/08/2012

@author: PauloLuan
'''
from zen.ce import cengine

class Projeto(object):
    
    def __init__(self, name, desc, link):
        self.name = name
        self.desc = desc
        self.link = link
    
    def save():
        
        
        
    def update():
        
        
    def delete():
        
    
    def getAllProjects():
        
    
    def getProject(id):
        
        
        
    def index(self):
        values = {"projetos_link": "/projetos", #cengine.handler_to_path(home.index 
                  "politicos_link": "/politicos", 
                  "mapa_link": "/mapa",
                  "sobre_link": "/sobre",
                  "aba_ativa": "projetos"}
        self.write_template("projetos.html", values)

    def about(self):
        self.write_template("about.html")
