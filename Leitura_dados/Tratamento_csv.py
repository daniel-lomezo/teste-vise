# -*- coding: utf-8 -*-


import os
import csv
from Leitura_dados.Tradutor import Google_Trad
from Leitura_dados.Conversor_moeda import Busca_moedas


class Tratamento_csv(object):
    def Exibe_dados_csv(self):
        with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'dados-complementares.csv')) as arquivo_csv:
            leitor_csv = csv.reader(arquivo_csv, delimiter=',')
            leitor_csv.__next__()
            for row in leitor_csv:
                cargo_traduzido = Google_Trad.Traduzindo_texto('0', row[1])
                market = Google_Trad.Traduzindo_texto('0', row[2])
                salario_AM = row[3].replace('$', '')
                cambio = Busca_moedas.Tratamento_moedas('0', 'Real')
                try:
                    salario_BR = float(salario_AM) / float(cambio)
                except ValueError:
                    salario_BR = 0
                print('')
                print(row[0] + ', ' + str(cargo_traduzido) + ', ' + market + ', ' + salario_AM + ', Salário convertido : ' + str((round(salario_BR, 2))))

