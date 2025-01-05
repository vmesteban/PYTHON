# Clase en vídeo: https://youtu.be/TbcEqkabAWU?t=19762

### Regular Expressions ###

import re

# match

my_string = "Esta es la lección número 7: Lección llamada Expresiones Regulares"
my_other_string = "Esta no es la lección número 6: Manejo de ficheros"

match = re.match("Esta es la lección", my_string, re.I)
print(match)
start, end = match.span()
print(my_string[start:end])

match = re.match("Esta no es la lección", my_other_string)
# if not(match == None): # Otra forma de comprobar el None
# if match != None: # Otra forma de comprobar el None
if match is not None:
    print(match)
    start, end = match.span()
    print(my_other_string[start:end])

print(re.match("Expresiones Regulares", my_string))

# search

search = re.search("lección", my_string, re.I)
print(search)
start, end = search.span()
print(my_string[start:end])

# findall

findall = re.findall("lección", my_string, re.I)
print(findall)

# split

print(re.split(":", my_string))

# sub

print(re.sub("[l|L]ección", "LECCIÓN", my_string))
print(re.sub("Expresiones Regulares", "RegEx", my_string))

# Clase en vídeo (09/11/22): https://www.twitch.tv/videos/1648023317

### Regular Expressions Patterns ###

# Para aprender y validar expresiones regulares: https://regex101.com

pattern = r"[lL]ección" # Que empiecen por l o por L
print(re.findall(pattern, my_string))

pattern = r"[lL]ección|Expresiones" # 'Que empiecen por l o por L' o que contenga la palabra 'Expresiones'
print(re.findall(pattern, my_string))

pattern = r"[0-9]" # que contengan dígitos
print(re.findall(pattern, my_string))
print(re.search(pattern, my_string))

pattern = r"\d" # que contengan dígitos
print(re.findall(pattern, my_string))

pattern = r"\D" # que solo contengan caracteres
print(re.findall(pattern, my_string))
print(re.findall(pattern, my_string))

pattern = r"[l]." # buscamos la 'l' y la letra de al lado
print(re.findall(pattern, my_string))

pattern = r"[l].*" # buscamos desde la 'l' a la frase completa
print(re.findall(pattern, my_string))


email = "mouredev@mouredev.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
# ^ que empieza por...
# [a-zA-Z0-9_.+-] que contenga numeros y letras y simbolos
# + sigue...
# @ contiene una "@"
# [a-zA-Z0-9_.+-] que contenga numeros y letras y simbolos
# + sigue...
# \. contiene un .
# [a-zA-Z-.] que contenga numeros y letras y simbolos
# + sigue...
# $ que acabe 
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "mouredev@mouredev.com.mx"
print(re.findall(pattern, email))
