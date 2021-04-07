# -*- coding: utf-8 -*-

from googlesearch import search

query = input("Enter you query: ")

for i in search(query, tld="com", num=10, stop=10, pause=2):
    print(i)



from googlesearch.googlesearch import GoogleSearch


busca = input("Digite o termo que deseja buscar: ")

results = GoogleSearch.search(GoogleSearch.parse_results(GoogleSearch, busca, google.com),query=busca, num_results= 5, prefetch_pages=True, num_prefetch_threads=10)

GoogleSearch.search()

print(googlesearch.search(results))
