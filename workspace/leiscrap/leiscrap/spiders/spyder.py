# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from leiscrap.items import LeiscrapItem

class LeisSpider(BaseSpider):
    name = "leis"
    allowed_domains = ["ceaam.net/sjc/legislacao/"]
    start_urls = [
                  "http://www.ceaam.net/sjc/legislacao/pesquisa.php?pesquisar=1&AnoIni=2012&AnoFim=2012&Tipo=Todos&Diploma=&Assunto=Todos&Texto=&Texto2=&Onde=Corpo"
                  ]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        leis = hxs.select('//div[@class="Lista"]')
        items = []
        
        for lei in leis:
            nomes = lei.select('a/b/text()').extract()
            links = lei.select('a/@href').extract()
            descs = lei.select('font/text()').extract()
            
            for i in range (len(nomes)):
                item = LeiscrapItem()
                item['name'] = nomes[i]
                item['link'] = 'http://www.ceaam.net/sjc/legislacao/'+ links[i]
                item['desc'] = descs[i]
                items.append(item)
    
        return items


"""
    URLs:
    
    Normativa - http://www.ceaam.net/sjc/legislacao/pesquisa.php?pesquisar=1&AnoIni=2012&AnoFim=2012&Tipo=Todos&Diploma=&Assunto=Todos&Texto=&Texto2=&Onde=Corpo
    Ementa - http://www.ceaam.net/sjc/legislacao/pesquisa.php?pesquisar=1&AnoIni=2012&AnoFim=2012&Tipo=Todos&Diploma=&Assunto=Todos&Texto=&Texto2=&Onde=Ementa
    ambos - http://www.ceaam.net/sjc/legislacao/pesquisa.php?pesquisar=1&AnoIni=2012&AnoFim=2012&Tipo=Todos&Diploma=&Assunto=Todos&Texto=&Texto2=&Onde=Ambos
    
    Todos - http://www.ceaam.net/sjc/legislacao/pesquisa.php?pesquisar=1&AnoIni=2012&AnoFim=2012&Tipo=Todos&Diploma=&Assunto=Todos&Texto=&Texto2=&Onde=Corpo
    
    Leis Ordinárias - http://www.ceaam.net/sjc/legislacao/pesquisa.php?pesquisar=1&AnoIni=2012&AnoFim=2012&Tipo=Lei%20Municipal&Diploma=&Assunto=Todos&Texto=&Texto2=&Onde=Ambos
    
    Leis Complementares -
    Decretos -
    Lei Orgânica -
    Regimento Interno & Resoluções -
    
    
    
    
    
    """
