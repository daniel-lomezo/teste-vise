from openpyxl import load_workbook
from Busca_cep import Requesicao_Cep
def ler_arquivo():
    arquivo_excel = load_workbook('dados-pessoais.xlsx')
    planilha1 = arquivo_excel['Página1']
    for i in range(1, 51 + 2):
        for j in range(1, 6 + 1):
            if planilha1.cell(row=i, column=j).value != None and planilha1.cell(row=i, column=j).value != '':

                print(planilha1.cell(row=i, column=j).value, end=" - ")
        if planilha1.cell(row=i, column=j).value != None and planilha1.cell(row=i, column=j).value != '':
            cep = Requesicao_Cep.Pesquisa_Cep('0', planilha1.cell(row=i, column=5).value)
            print('Endereço completo: {}'.format(cep))

        print('')
        print('')
        print('')
ler_arquivo()