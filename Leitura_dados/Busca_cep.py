# -*- coding: utf-8 -*-

import requests

class Requesicao_Cep(object):

    def Pesquisa_Cep(self, cep):
        for char in cep:
            if char in " ?.!/;:-CEP":
                cep.replace(char, '')
        url = 'https://viacep.com.br/ws/{}/json/'.format(cep)
        r = requests.request('GET', url)
        if cep == 'CEP':
            return {'erro':'Não encontrado'}
        resposta_cep = r.json()
        if resposta_cep.get('erro'):
            return {'erro':'Endereço não encontrado'}
        resposta_cep.pop('cep')
        return resposta_cep
