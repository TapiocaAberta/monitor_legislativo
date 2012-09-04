# Scrapy settings for leiscrap project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/topics/settings.html
#

BOT_NAME = 'leiscrap'
BOT_VERSION = '1.0'

SPIDER_MODULES = ['leiscrap.spiders']
NEWSPIDER_MODULE = 'leiscrap.spiders'
USER_AGENT = '%s/%s' % (BOT_NAME, BOT_VERSION)

