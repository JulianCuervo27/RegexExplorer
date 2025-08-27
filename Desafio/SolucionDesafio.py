import re

texto='En el archivo de configuración aparece "usuario" con nivel 3, el puntaje promedio fue 4.75, la opción "activo" está marcada como True, mientras que "verificado" está en False, y además se registran listas como [1, 2, 3], [-5, 10, 15] y [0.5, 1.5, 2.5].'

patron1 = r"-?\b\d+\b"
enteros = re.findall(patron1, texto)

patron2 = r"[+-]?\d+(?:\.\d+)?"
flotantes = re.findall(patron2, texto)

patron3 = r"\b(True|False)\b"
booleans = re.findall(patron3, texto, re.IGNORECASE)

patron4 = r'"(.*?)"'
strings = re.findall(patron4, texto)

patron5 = r"\[[^\]]+\]"
listas = re.findall(patron5, texto)
print(texto)

print("\nEnteros encontrados: ",enteros)
print("Cantidad de enteros: ",len(enteros))
print("\nFlotantes encontrados: ",flotantes)
print("Cantidad de Flotantes: ",len(flotantes))
print("\nBooleanos encontrados: ",booleans)
print("Cantidad de Booleanos: ",len(booleans))
print("\nStrings encontrados: ",strings)
print("Cantidad de strings: ",len(strings))
print("\nListas encontradas: ",listas)
print("Cantidad de listas: ",len(listas))
