#-*- coding: utf-8 -*-
'''
Created on 13/08/2012

@author: PauloLuan
'''
from __future__ import unicode_literals
from projetos.model import Projeto
from zen.ce import cengine
import logging
from politicos.model import Politico

class home():
    def index(self):
        # self.initialize_politicos()
        politicos = Politico.find_all()
        #politicos = self.lista_politicos
        search_url = cengine.to_path(home.search)
        values = {
            "aba_ativa": "politicos",
            "politicos": politicos,
            "search_url": search_url,
            }
        self.write_template("politicos.html", values)

    def search(self):
        nome = self.get('nome')
        politicos = Politico.find_by_name(nome)
        values = {
            "aba_ativa": "politicos",
            "politicos": politicos
        }
        self.write_template("politicos.html", values)

    def perfil(self, key_politico):
        politico = Politico.find_politico(key_politico)
        logging.info("Atributos!!! /n Nome:" + politico.nome + "/n descricao: " + politico.descricao)
        projetos = Projeto.find_tree_projects()
        values = {"aba_ativa": "politicos",
                  "politico": politico,
                  "projetos": projetos
        }
        self.write_template("perfilPolitico.html", values)


class edit():
    def index(self):
        politicos = Politico.find_all()
        search_url = cengine.to_path(home.search)
        values = {
            "aba_ativa": "politicos",
            "politicos": politicos,
            "search_url": search_url,
            }
        self.write_template("list_edit_politicos.html", values)

    def edit_politico(self, key_politico):
        politico = Politico.find_politico(key_politico)
        values = {"aba_ativa": "politicos",
                  "politico": politico,
                  "save_url": cengine.to_path(edit.save_edit)
        }
        self.write_template("edit_politicos.html", values)

    def delete(self, id_politico):
        Politico.delete(id_politico)
        self.redirect(cengine.to_path(edit.index))

    def save_edit(self):
        key = self.get("key_politico")
        politico = Politico.find_politico(key)

        politico.nome = self.get("nome")
        politico.partido = self.get("partido")
        politico.foto = self.get("foto")
        politico.dados = self.get("dados")
        politico.email = self.get("email")
        politico.telefone = self.get("telefone")
        politico.localtrabalho = self.get("localtrabalho")
        politico.descricao = self.get("descricao")

        politico.put()
        self.redirect(cengine.to_path(edit.index))

    def new(self):
        values = {"aba_ativa": "politicos",
                  "save_url": cengine.to_path(edit.save_new)
        }
        self.write_template("create_politico.html", values)

    def save_new(self):
        politico = Politico(
            nome=self.get("nome"),
            partido=self.get("partido"),
            descricao=self.get("descricao"),
            foto=self.get("foto"),
            dados=self.get("dados"),
            email=self.get("email"),
            telefone=self.get("telefone"),
            localtrabalho=self.get("localtrabalho")
        )
        politico.put()
        self.redirect(cengine.to_path(edit.index))


class initialize():
    lista_politicos = [{
        "id_politico": "1",
        "nome": "Alexandre da Farmácia",
        "partido": "PP",
        "foto": "alexandre",
        #"foto": "http://camarasjc.sp.tempsite.ws/clicknow/arquivo/thumb/vereadores/0fe7811bcda01c21e43c_120x120_1_0.jpg",
        "dados": "Alexandre José da Cunha, nascido no dia 26/04/70, em São José dos Campos (SP). Comerciante.",
        "email": "alexandrefarm@camarasjc.sp.gov.br",
        "telefone": "(12) 3925-6568",
        "localtrabalho": "Sala 09 - Térreo",
        "descricao": "Eleito vereador em 1996, aos 26 anos. Já no primeiro mandato se dedicou ao trabalho em parceria com a comunidade. Em 2000, foi reeleito vereador mais votado da cidade. É autor de importantes projetos de lei como: obriga médicos da rede pública a receitarem os medicamentos pelo nome genérico; cria parcerias para levar água a loteamentos irregulares; aumenta o valor da multa para donos de terrenos sujos; valoriza o doador de sague. Atualmente cumpre o 4º mandato e foi presidente da Câmara Municipal no biênio 2009/2010 Legislatura: 4º mandato (de 1997/2012)"
    },
            {
            "id_politico": "2",
            "nome": "Amélia Naomi",
            "partido": "PT",
            "foto": "amelia",
            #"foto": "http://camarasjc.sp.tempsite.ws/clicknow/arquivo/thumb/vereadores/6b481948561443988368_120x120_1_0.jpg",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "3",
            "nome": "Angela Guadagnin",
            "partido": "PT",
            "foto": "angela",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"
        },
            {
            "id_politico": "4",
            "nome": "Cristiano Pinto Ferreira",
            "partido": "PV",
            "foto": "cristiano",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "5",
            "nome": "Cristóvão Gonçalves",
            "partido": "PSDB",
            "foto": "cristovao",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "6",
            "nome": "Dilermando Dié",
            "partido": "PSDB",
            "foto": "dilermando",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "7",
            "nome": "Dulce Rita",
            "partido": "PSDB",
            "foto": "dulce",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "8",
            "nome": "Jairo Santos",
            "partido": "PV",
            "foto": "jairo",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "9",
            "nome": "João das Mercês Tampão",
            "partido": "PTB",
            "foto": "joao",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "10",
            "nome": "Juvenil Silvério",
            "partido": "PSDB",
            "foto": "juvenil",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "11",
            "nome": "Luiz Mota",
            "partido": "DEM",
            "foto": "luiz",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "12",
            "nome": "Macedo Bastos",
            "partido": "DEM",
            "foto": "macedo",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "13",
            "nome": "Miranda Ueb",
            "partido": "PPS",
            "foto": "miranda",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "14",
            "nome": "Petiti da Farmácia Comunitária",
            "partido": "PSDB",
            "foto": "petiti",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "15",
            "nome": "Renata Paiva",
            "partido": "DEM",
            "foto": "renata",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "16",
            "nome": "Robertinho da Padaria",
            "partido": "PPS",
            "foto": "robertinho",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "17",
            "nome": "Tonhão Dutra",
            "partido": "PT",
            "foto": "tonhao",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "18",
            "nome": "Vadinho Covas",
            "partido": "PSDB",
            "foto": "vadinho",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "19",
            "nome": "Valdir Alvarenga",
            "partido": "PSB",
            "foto": "valdir",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"

        },
            {
            "id_politico": "20",
            "nome": "Wagner Balieiro",
            "partido": "PT",
            "foto": "wagner",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"
        },
            {
            "id_politico": "21",
            "nome": "Walter Hayashi",
            "partido": "PSB",
            "foto": "walter",
            "dados": "dados",
            "email": "email",
            "telefone": "telefone",
            "localtrabalho": "local",
            "descricao": "descrição"
        }
    ]

    def index(self):
        for politico in self.lista_politicos:
            p = Politico(
                id_politico=politico["id_politico"],
                nome=politico["nome"],
                partido=politico["partido"],
                foto=politico["foto"],
                dados=politico["dados"],
                email=politico["email"],
                telefone=politico["telefone"],
                localtrabalho=politico["localtrabalho"],
                descricao=politico["descricao"]
            )
            p.put()

        projetos = [{
            "id_projeto": "1",
            "nota": 40,
            "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0470.htm",
            "nome": " LEI COMPLEMENTAR Nº 470, DE 10/08/2012",
            "descricao": "Autoriza o Poder Executivo, por intermédio da Secretaria de Educação, a celebrar convênio com o Centro Promocional de Eugênio de Melo, objetivando o desenvolvimento do Centro de Educação Infantil - CEDIN - Amália Bondesan dos Santos, no Distrito de Eugênio de Melo, para atendimento em período integral de crianças de zero a cinco anos de idade, filhos de mães com atividades remuneradas e de baixa renda, e dá outras providências."
        },
                {
                "id_projeto": "2",
                "nota": 60,
                "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0469.htm",
                "nome": " LEI COMPLEMENTAR Nº 469, DE 04/07/2012",
                "descricao": "Altera a redação da ementa e do artigo 1º da projeto Complementar nº 309, de 08 de dezembro de 2006, que \"autoriza o Executivo Municipal a contratar pessoal, por prazo determinado, para atender as necessidades do 'Programa de Agentes Comunitários de Saúde' - PACS -, do Governo Federal\", e a redação da ementa e do artigo 1º da projeto Complementar nº 326, de 05 de julho de 2007, que \"autoriza o Poder Executivo a contratar pessoal, por prazo determinado, para atender às necessidades do 'Sistema Nacional de Vigilância em Saúde' no combate às endemias, do Governo Federal, nos termos da Portaria nº 1.172, de 15 de junho de 2004, com suas posteriores alterações\"."
            },
                {
                "id_projeto": "3",
                "nota": 100,
                "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0468.htm",
                "nome": " LEI COMPLEMENTAR Nº 468, DE 04/07/2012",
                "descricao": "Desafeta as áreas de domínio público municipal que especifica, classificando-as como bens dominicais, autoriza a Prefeitura Municipal a doá-las à Companhia de Desenvolvimento Habitacional e Urbano do Estado de São Paulo - CDHU -, para a implantação de programa habitacional no Município, e dá outras providências."
            },
                {
                "id_projeto": "4",
                "nota": 10,
                "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0467.htm",
                "nome": " LEI COMPLEMENTAR Nº 467, DE 26/04/2012",
                "descricao": "Acrescenta um artigo 52-B à projeto Complementar nº 56, de 24 de julho de 1992, que \"Dispõe sobre o Estatuto dos Servidores Públicos do Município, de suas Fundações e Autarquias\", e altera a projeto Complementar nº 452, de 08 de dezembro de 2011, que \"Reestrutura a Secretaria de Administração e a Secretaria de Assuntos Jurídicos, e dá outras providências\"."
            },
                {
                "id_projeto": "5",
                "nota": 35,
                "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0466.htm",
                "nome": " LEI COMPLEMENTAR Nº 466, DE 19/04/2012",
                "descricao": "Altera a redação do inciso III, do artigo 3º da projeto nº 4.269, de 11 de setembro de 1992, com as alterações introduzidas pela projeto Complementar nº 463, de 28 de fevereiro de 2012, pela projeto Complementar nº 367, de 10 de junho de 2008 e pela projeto Complementar nº 412, de 21 de dezembro de 2009, que \"Cria o Conselho Municipal de Segurança\"."
            },
                {
                "id_projeto": "6",
                "nota": 40,
                "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0465.htm",
                "nome": " LEI COMPLEMENTAR Nº 465, DE 28/03/2012",
                "descricao": "Altera o valor da remuneração de que trata o artigo 8º da projeto Complementar nº 309, de 08 de dezembro de 2006, com suas alterações, e o valor da remuneração de que trata o artigo 8º da projeto Complementar nº 326, de 05 de julho de 2007, com suas alterações, e dá outras providências."
            },
                {
                "id_projeto": "7",
                "nota": 75,
                "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0464.htm",
                "nome": " LEI COMPLEMENTAR Nº 464, DE 23/03/2012",
                "descricao": "Autoriza o Poder Executivo a outorgar concessão de direito real de uso de uma área de domínio público municipal ao Serviço Social do Comércio - SESC, e dá outras providências."
            },
                {
                "id_projeto": "8",
                "nota": 97,
                "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/Lc0463.htm",
                "nome": " LEI COMPLEMENTAR Nº 463, DE 28/02/2012",
                "descricao": "Altera a redação do inciso III, do artigo 3º da projeto nº 4.269, de 11 de setembro de 1992, com as alterações introduzidas pela projeto Complementar nº 367, de 10 de junho de 2008 e pela projeto Complementar nº 412, de 21 de dezembro de 2009, que \"Cria o Conselho Municipal de Segurança\"."
            },
                {
                "id_projeto": "9",
                "nota": 40,
                "link": "http://www.ceaam.net/sjc/legislacao/leis/2012/L8781.htm",
                "nome": " LEI MUNICIPAL Nº 8.781, DE 10/08/2012",
                "descricao": "Autoriza o Poder Executivo, por intermédio da Secretaria de Educação, a celebrar convênio com a Fundação Valeparaibana de Ensino, objetivando o desenvolvimento do Centro de Educação Infantil - CEDIN - Maria Aparecida Barboza Pedroza, no Jardim Telespark, para atendimento em período integral de crianças de zero a cinco anos de idade, filhos de mães com atividades remuneradas e de baixa renda, e dá outras providências."
            }
        ]

        for projeto in projetos:
            lei = Projeto(
                nome=projeto["nome"],
                nota=projeto["nota"],
                link=projeto["link"],
                descricao=projeto["descricao"]
            )
            lei.put()

        self.redirect("/politicos/edit")