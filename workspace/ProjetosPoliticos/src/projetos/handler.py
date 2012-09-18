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
                  "aba_ativa": "projetos",
        
        "leis" : [
                {
                    "id_projeto": "1",
                    "nota": 40,
                    "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0470.htm",
                    "name": " LEI COMPLEMENTAR Nº 470, DE 10/08/2012",
                    "desc": "Autoriza o Poder Executivo, por intermédio da Secretaria de Educação, a celebrar convênio com o Centro Promocional de Eugênio de Melo, objetivando o desenvolvimento do Centro de Educação Infantil - CEDIN - Amália Bondesan dos Santos, no Distrito de Eugênio de Melo, para atendimento em período integral de crianças de zero a cinco anos de idade, filhos de mães com atividades remuneradas e de baixa renda, e dá outras providências."
                },
                {
                    "id_projeto": "2",
                    "nota": 60,
                    "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0469.htm",
                    "name": " LEI COMPLEMENTAR Nº 469, DE 04/07/2012",
                    "desc": "Altera a redação da ementa e do artigo 1º da Lei Complementar nº 309, de 08 de dezembro de 2006, que \"autoriza o Executivo Municipal a contratar pessoal, por prazo determinado, para atender as necessidades do 'Programa de Agentes Comunitários de Saúde' - PACS -, do Governo Federal\", e a redação da ementa e do artigo 1º da Lei Complementar nº 326, de 05 de julho de 2007, que \"autoriza o Poder Executivo a contratar pessoal, por prazo determinado, para atender às necessidades do 'Sistema Nacional de Vigilância em Saúde' no combate às endemias, do Governo Federal, nos termos da Portaria nº 1.172, de 15 de junho de 2004, com suas posteriores alterações\"."
                },
                {
                    "id_projeto": "3",
                    "nota": 100,
                    "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0468.htm",
                    "name": " LEI COMPLEMENTAR Nº 468, DE 04/07/2012",
                    "desc": "Desafeta as áreas de domínio público municipal que especifica, classificando-as como bens dominicais, autoriza a Prefeitura Municipal a doá-las à Companhia de Desenvolvimento Habitacional e Urbano do Estado de São Paulo - CDHU -, para a implantação de programa habitacional no Município, e dá outras providências."
                },
                {
                    "id_projeto": "4",
                    "nota": 10,
                    "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0467.htm",
                    "name": " LEI COMPLEMENTAR Nº 467, DE 26/04/2012",
                    "desc": "Acrescenta um artigo 52-B à Lei Complementar nº 56, de 24 de julho de 1992, que \"Dispõe sobre o Estatuto dos Servidores Públicos do Município, de suas Fundações e Autarquias\", e altera a Lei Complementar nº 452, de 08 de dezembro de 2011, que \"Reestrutura a Secretaria de Administração e a Secretaria de Assuntos Jurídicos, e dá outras providências\"."
                },
                {
                    "id_projeto": "5",
                    "nota": 35,
                    "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0466.htm",
                    "name": " LEI COMPLEMENTAR Nº 466, DE 19/04/2012",
                    "desc": "Altera a redação do inciso III, do artigo 3º da Lei nº 4.269, de 11 de setembro de 1992, com as alterações introduzidas pela Lei Complementar nº 463, de 28 de fevereiro de 2012, pela Lei Complementar nº 367, de 10 de junho de 2008 e pela Lei Complementar nº 412, de 21 de dezembro de 2009, que \"Cria o Conselho Municipal de Segurança\"."
                },
                {
                    "id_projeto": "6",
                    "nota": 40 ,
                    "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0465.htm",
                    "name": " LEI COMPLEMENTAR Nº 465, DE 28/03/2012",
                    "desc": "Altera o valor da remuneração de que trata o artigo 8º da Lei Complementar nº 309, de 08 de dezembro de 2006, com suas alterações, e o valor da remuneração de que trata o artigo 8º da Lei Complementar nº 326, de 05 de julho de 2007, com suas alterações, e dá outras providências."
                },
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
                },
                {
                    "id_projeto": "9",
                    "nota": 40,
                    "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/L8781.htm",
                    "name": " LEI MUNICIPAL Nº 8.781, DE 10/08/2012",
                    "desc": "Autoriza o Poder Executivo, por intermédio da Secretaria de Educação, a celebrar convênio com a Fundação Valeparaibana de Ensino, objetivando o desenvolvimento do Centro de Educação Infantil - CEDIN - Maria Aparecida Barboza Pedroza, no Jardim Telespark, para atendimento em período integral de crianças de zero a cinco anos de idade, filhos de mães com atividades remuneradas e de baixa renda, e dá outras providências."
                }]}
        
        self.write_template("projetos.html", values)

    def about(self):
        self.write_template("about.html")
