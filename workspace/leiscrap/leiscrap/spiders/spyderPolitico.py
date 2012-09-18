# -*- coding: utf-8 -*-
# This package will contain the spiders of your Scrapy project
#
# Please refer to the documentation for information on how to create and manage
# your spiders.

from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from leiscrap.items import PoliticoscrapItem

class PoliticoSpider(BaseSpider):
    name = "politicos"
    allowed_domains = ["http://camarasjc.sp.tempsite.ws/"]
    start_urls = [
                  "http://camarasjc.sp.tempsite.ws/clicknow/vereadores/"
                  ]
    
    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        lis = hxs.select('//div[@class="listagem"]/ul/li')
        
	vereadores = []
        
        for li in lis:
	    table = li.select('table/tbody/tr/td')
	    print table
	
	"""
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

