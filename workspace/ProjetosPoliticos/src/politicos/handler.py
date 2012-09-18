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
                  "sobre_link": "/sobre",
                  "aba_ativa": "politicos",
                  
                  "politicos":[
                        {
                            "nome": "Alexandre da Farmácia",
                            "partido": "PP",
                            "foto": "alexandre"
                        },
                        {
                            "nome": "Amélia Naomi",
                            "partido": "PT",
                            "foto": "amelia"
                        },
                        {
                            "nome": "Angela Guadagnin",
                            "partido": "PT",
                            "foto": "angela"
                        },
                        {
                            "nome": "Cristiano Pinto Ferreira",
                            "partido": "PV",
                            "foto": "cristiano"
                        },
                        {
                            "nome": "Cristóvão Gonçalves",
                            "partido": "PSDB",
                            "foto": "cristovao"
                        },
                        {
                            "nome": "Dilermando Dié",
                            "partido": "PSDB",
                            "foto": "dilermando"
                        },
                        {
                            "nome": "Dulce Rita",
                            "partido": "PSDB",
                            "foto": "dulce"
                        },
                        {
                            "nome": "Jairo Santos",
                            "partido": "PV",
                            "foto": "jairo"
                        },
                        {
                            "nome": "João das Mercês Tampão",
                            "partido": "PTB",
                            "foto": "joao"
                        },
                        {
                            "nome": "Juvenil Silvério",
                            "partido": "PSDB",
                            "foto": "juvenil"
                        },
                        {
                            "nome": "Luiz Mota",
                            "partido": "DEM",
                            "foto": "luiz"
                        },
                        {
                            "nome": "Macedo Bastos",
                            "partido": "DEM",
                            "foto": "macedo"
                        },
                        {
                            "nome": "Miranda Ueb",
                            "partido": "PPS",
                            "foto": "miranda"
                        },
                        {
                            "nome": "Petiti da Farmácia Comunitária",
                            "partido": "PSDB",
                            "foto": "petiti"
                        },
                        {
                            "nome": "Renata Paiva",
                            "partido": "DEM",
                            "foto": "renata"
                        },
                        {
                            "nome": "Robertinho da Padaria",
                            "partido": "PPS",
                            "foto": "robertinho"
                        },
                        {
                            "nome": "Tonhão Dutra",
                            "partido": "PT",
                            "foto": "tonhao"
                        },
                        {
                            "nome": "Vadinho Covas",
                            "partido": "PSDB",
                            "foto": "vadinho"
                        },
                        {
                            "nome": "Valdir Alvarenga",
                            "partido": "PSB",
                            "foto": "valdir"
                        },
                        {
                            "nome": "Wagner Balieiro",
                            "partido": "PT",
                            "foto": "wagner"
                        },
                        {
                            "nome": "Walter Hayashi",
                            "partido": "PSB",
                            "foto": "walter"
                        }
                    ]
        }
        
        self.write_template("politicos.html", values)
        
    def perfil(self):
        values = {
              "projetos_link": "/projetos", #cengine.handler_to_path(home.index 
              "politicos_link": "/politicos",
              "mapa_link": "/mapa",
              "sobre_link": "/sobre",
              "aba_ativa": "politicos",
              "perfil" : []               
        }
        self.write_template("perfilPolitico.html")
