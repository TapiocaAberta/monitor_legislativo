#-*- coding: utf-8 -*-
'''
Created on 13/08/2012

@author: PauloLuan
'''

from __future__ import unicode_literals
from zen.ce import cengine
from google.appengine.api import users

class home():
    def index(self):
        values = {
                  "aba_ativa": "sobre",
                  }
        self.write_template('about.html', values)
    
