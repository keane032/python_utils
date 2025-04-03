import requests
import language_tool_python 
from bs4 import BeautifulSoup

tool = language_tool_python.LanguageTool("pt-BR")

url = "https://integrasus.saude.ce.gov.br/"

response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

head = soup.head

print("=== HEADERS DO HTML ===")
for tag in head.find_all(["title"]):
    error = tool.check(tag.text)
   
    if error:
        print(f" Foram encontrados {len(error)} erros de português:")
        for erro in error:
            print(f"- {erro.ruleId}: {erro.message} (Sugestão: {erro.replacements})")
    else:
        print(" Nenhum erro de português encontrado!")
    print(tag.text)