# -*- coding: utf-8 -*-


import googlesearch
from google_utils import Google

busca = input("Digite o termo que deseja buscar: ")

results = Google.search(busca)

print(googlesearch.search(busca, num_results=10, lang="pt"))
