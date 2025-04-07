import requests
import language_tool_python 
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time

tool = language_tool_python.LanguageTool("pt-BR")

url = input("Url: ")

optionsChrome = Options()
optionsChrome.add_argument("--headless")
driver = webdriver.Chrome(options=optionsChrome)
driver.get(url)
time.sleep(5)

# response = requests.get(url)
# soup = BeautifulSoup(response.text, "html.parser")
# print(soup)
# head = soup.head <<< trocar para body

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")

print("=== HEADERS DO HTML ===")
for tag in soup.find_all(["mat-card-title"]):
    error = tool.check(tag.text)
    print(f"{tag.name} - {tag.text}")
    if error:
        print(f" Foram encontrados {len(error)} erros de português:")
        for erro in error:
            print(f"- {erro.ruleId}: {erro.message} (Sugestão: {erro.replacements})")
    else:
        print(" Nenhum erro de português encontrado!")