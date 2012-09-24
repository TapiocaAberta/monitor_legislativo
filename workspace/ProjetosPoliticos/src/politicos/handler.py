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
                                "id_politico": "1",
                                "nome": "Alexandre da Farmácia",
                                "partido": "PP",
                                "foto": "alexandre"
                                },
                                {
                                "id_politico": "2",
                                "nome": "Amélia Naomi",
                                "partido": "PT",
                                "foto": "amelia"
                                },
                                {
                                "id_politico": "3",
                                "nome": "Angela Guadagnin",
                                "partido": "PT",
                                "foto": "angela"
                                },
                                {
                                "id_politico": "4",
                                "nome": "Cristiano Pinto Ferreira",
                                "partido": "PV",
                                "foto": "cristiano"
                                },
                                {
                                "id_politico": "5",
                                "nome": "Cristóvão Gonçalves",
                                "partido": "PSDB",
                                "foto": "cristovao"
                                },
                                {
                                "id_politico": "6",
                                "nome": "Dilermando Dié",
                                "partido": "PSDB",
                                "foto": "dilermando"
                                },
                                {
                                "id_politico": "7",
                                "nome": "Dulce Rita",
                                "partido": "PSDB",
                                "foto": "dulce"
                                },
                                {
                                "id_politico": "8",
                                "nome": "Jairo Santos",
                                "partido": "PV",
                                "foto": "jairo"
                                },
                                {
                                "id_politico": "9",
                                "nome": "João das Mercês Tampão",
                                "partido": "PTB",
                                "foto": "joao"
                                },
                                {
                                "id_politico": "10",
                                "nome": "Juvenil Silvério",
                                "partido": "PSDB",
                                "foto": "juvenil"
                                },
                                {
                                "id_politico": "11",
                                "nome": "Luiz Mota",
                                "partido": "DEM",
                                "foto": "luiz"
                                },
                                {
                                "id_politico": "12",
                                "nome": "Macedo Bastos",
                                "partido": "DEM",
                                "foto": "macedo"
                                },
                                {
                                "id_politico": "13",
                                "nome": "Miranda Ueb",
                                "partido": "PPS",
                                "foto": "miranda"
                                },
                                {
                                "id_politico": "14",
                                "nome": "Petiti da Farmácia Comunitária",
                                "partido": "PSDB",
                                "foto": "petiti"
                                },
                                {
                                "id_politico": "15",
                                "nome": "Renata Paiva",
                                "partido": "DEM",
                                "foto": "renata"
                                },
                                {
                                "id_politico": "16",
                                "nome": "Robertinho da Padaria",
                                "partido": "PPS",
                                "foto": "robertinho"
                                },
                                {
                                "id_politico": "17",
                                "nome": "Tonhão Dutra",
                                "partido": "PT",
                                "foto": "tonhao"
                                },
                                {
                                "id_politico": "18",
                                "nome": "Vadinho Covas",
                                "partido": "PSDB",
                                "foto": "vadinho"
                                },
                                {
                                "id_politico": "19",
                                "nome": "Valdir Alvarenga",
                                "partido": "PSB",
                                "foto": "valdir"
                                },
                                {
                                "id_politico": "20",
                                "nome": "Wagner Balieiro",
                                "partido": "PT",
                                "foto": "wagner"
                                },
                                {
                                "id_politico": "21",
                                "nome": "Walter Hayashi",
                                "partido": "PSB",
                                "foto": "walter"
                                }
                               ]
                  }
        self.write_template("politicos.html", values)
        
    def perfil(self):
        values = {"projetos_link": "/projetos", #cengine.handler_to_path(home.index 
                  "politicos_link": "/politicos",
                  "mapa_link": "/mapa",
                  "sobre_link": "/sobre",
                  "aba_ativa": "politicos",
                  "politico" : {"id_politico": "1",
                               "nome": "Alexandre da Farmácia",
                               "partido": "PP",
                               "foto": "alexandre"},
                  "leis" : [
                            {
                             "id_projeto": "7",
                             "nota": 75,
                             "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0464.htm",
                             "name": " LEI COMPLEMENTAR Nº 464, DE 23/03/2012",
                             "desc": "Autoriza o Poder Executivo a outorgar concessão de direito real de uso de uma área de domínio público municipal ao Serviço Social do Comércio - SESC, e dá outras providências."
                            },
                            {
                             "id_projeto": "8",
                             "nota": 97,
                             "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0463.htm",
                             "name": " LEI COMPLEMENTAR Nº 463, DE 28/02/2012",
                             "desc": "Altera a redação do inciso III, do artigo 3º da Lei nº 4.269, de 11 de setembro de 1992, com as alterações introduzidas pela Lei Complementar nº 367, de 10 de junho de 2008 e pela Lei Complementar nº 412, de 21 de dezembro de 2009, que \"Cria o Conselho Municipal de Segurança\"."
                            }
                            ]
                  }
        self.write_template("perfilPolitico.html", values)
