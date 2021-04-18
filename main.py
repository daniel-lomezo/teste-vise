# Esse progama tme como objetivo tratar os dados de fontes diferentes
# Um arquivo csv, xls e um web-service

from Leitura_dados.Busca_cep import Requesicao_Cep

print('Temos as seguintes opções: \n')
print('Para visualizar todos os dados pessoais, digite 1')
print('Para visualizar todos os dados complementares, digite 2')
print('Para buscar informações combinadas dirto dos arquivos, digite 3')
print('Para inserir as informações de um funcionáio na base de dados, digite 4')
print('Para inserir os dados de todos os funcionários, digite 5 \n')
print('Para sair digite 6')

menu = input('Aguardando a opção desejada para continuar ! \n')
class Init(object):
    def Menu(self, menu):
        quit = True
        while quit:
            if str(menu) =='1':
                pass

            elif str(menu) == 2:
                pass

            elif str(menu) == 3:
                pass

            elif str(menu) == 4:
                pass

            elif str(menu) == 5:
                pass

            elif str(menu) == 6:
                quit = False


            else:
                print('Essa não é uma opção válida')

if __name__ == '__main__':
    Init.Menu('0', menu)
