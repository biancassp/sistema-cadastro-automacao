#Ler dados da planilha 
#Inserir cada célula de cada linha em um campo do sistema
import openpyxl 
import pyautogui

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

workbook = openpyxl.load_workbook('vendas_de_produtos.xlsx')
vendas_sheet = workbook['vendas']

for linha in vendas_sheet.iter_rows(min_row=2):
    #nome
    pyautogui.click(994,126,duration=1.0)
    pyautogui.write(linha[0].value)
    #produto
    pyautogui.click(997,152,duration=1.0)
    pyautogui.write(linha[1].value)
    #quantidade
    pyautogui.click(1011,178,duration=1.0)
    pyautogui.write(str(linha[2].value))
    #categoria
    pyautogui.click(1073,204,duration=1.0)
    pyautogui.write(linha[3].value)
    #salvar
    pyautogui.click(943,232,duration=1.0)
    #ok
    pyautogui.click(653,426,duration=1.0)
   