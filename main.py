# -*- coding: utf-8 -*-

# Esse progama tme como objetivo tratar os dados de fontes diferentes
# Um arquivo csv, xls e um web-service

from Leitura_dados.Tratamento_xls import Tratamento_arquivo
from Leitura_dados.Tratamento_csv import Tratamento_csv
from Leitura_dados.Db_func import Conn_db

print('Temos as seguintes opções: \n')
print('Para visualizar todos os dados pessoais, digite 1')
print('Para visualizar todos os dados complementares, digite 2')
print('Para inserir todos os dados na base de dados, digite 3')
print('Para sair digite 6 \n')

class Init(object):
    def Menu(self):
        quit = True
        while quit:
            menu = input('Aguardando a opção desejada para continuar ! \n')
            if str(menu) == '1':
                Tratamento_arquivo.Visualizar_dados('0')
            elif str(menu) == '2':
                Tratamento_csv.Exibe_dados_csv('0')
            elif str(menu) == '3':
                Conn_db.Insere_dados('0')
            elif str(menu) == '6':
                quit = False
            else:
                print('Essa não é uma opção válida')

if __name__ == '__main__':
    Init.Menu('0')
