import bs4
import requests

# crear una url sin numero de pagina
url_base="http://books.toscrape.com/catalogue/page-{}.html"

# lista de titulos con 4 o 5 estrellas
titulos_rating_alto=[]

#iterar paginas
for pagina in range(1,11):
    #crear sopa en cada pagina
    url_pagina=url_base.format(pagina)
    resultado=requests.get(url_pagina)
    sopa=bs4.BeautifulSoup(resultado.text, "lxml")

    #extraer titulos y rating
    libros=sopa.select(".product_pod")

    #iterar en los libros
    for libro in libros:
        #chequear que tengan 4 o 5 estrellas
        if len(libro.select(".star-rating.Four"))!=0 or len(libro.select(".star-rating.Five"))!=0:
            #guardar el titulo
            titulo_libro=libro.select("a")[1]["title"]
            #guardar el titulo en la lista de titulos con 4 o 5 estrellas
            titulos_rating_alto.append(titulo_libro)

# imprimir los titulos
indice=0
for titulo in titulos_rating_alto:
    indice+=1
    print(f"\n{indice} - {titulo}")
    print(titulo)
