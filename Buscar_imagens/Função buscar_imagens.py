from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import webbrowser

# Mostrar url usando o navegador padrão. Se o novo for 0, a url é aberto na mesma janela do navegador,
# se possível. Se é novo 1, uma nova janela do navegador é aberto, se possível.

webbrowser.open('www.google.com', new=0, autoraise=True)





chrome_options = Options()
chrome_options.add_argument("--headless")

print('Aguarde, os dados estão sendo coletados...')

tempo_inicial = time.time()
driver = webdriver.Chrome(options=chrome_options)
driver.get('https://www.google.com/search?q=tesla')

html = driver.page_source

soup = BeautifulSoup(html,'html.parser')
img_tesla = soup.find('g-img', class_='ivg-i')
endereco_imagem = img_tesla.get('data-lpage')
tempo_final = time.time()
print(f'Endereço da imagem: {endereco_imagem}')
print(f'Tempo de coleta: {tempo_final-tempo_inicial:.2f} segundos')