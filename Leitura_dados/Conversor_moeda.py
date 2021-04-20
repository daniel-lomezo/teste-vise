# -*- coding: utf-8 -*-
import requests
import xml.etree.ElementTree as ET


class Busca_moedas(object):
    def Tratamento_moedas(self, option):
        url = 'https://www.ecb.europa.eu/stats/eurofxref/eurofxref-daily.xml'
        resposta = requests.get(url)
        root = ET.fromstring(resposta.content)
        for child in root.iter('{http://www.ecb.int/vocabulary/2002-08-01/eurofxref}Cube'):
            var = child.attrib
            qt = len(var)
            if qt == 2:
               if var['currency'] == 'BRL':
                   real = var['rate']
               if var['currency'] == 'USD':
                   dolar = var['rate']
        if option == 'converter':
            convert = float(dolar) / float(real)
            return convert
        if option == 'Dolar':
            return dolar
        if option == 'Real':
            return real

