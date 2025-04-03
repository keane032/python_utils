import openpyxl
from urllib.parse import quote
import webbrowser
import pyautogui
from time import sleep

data = openpyxl.load_workbook('dados.xlsx')

pagina = data.active

for linha in pagina.iter_rows(min_row=2):
    nome = linha[0].value
    telefone = int(linha[1].value)
    print(telefone)
    msg = '...'
    url = f'https://web.whatsapp.com/send?phone={telefone}&text={quote(msg)}'
    print(url)
    webbrowser.open(url=url)
    sleep(10)
    pyautogui.press('enter')
    sleep(5)
    pyautogui.hotkey('ctrl', 'w')
