# Mapeo fijo de cifrado
mapeo_cifrado = {
    'a': 'q', 'b': 'w', 'c': 'e', 'd': 'r', 'e': 't',
    'f': 'y', 'g': 'u', 'h': 'i', 'i': 'o', 'j': 'p',
    'k': 'a', 'l': 's', 'm': 'd', 'n': 'f', 'o': 'g',
    'p': 'h', 'q': 'j', 'r': 'k', 's': 'l', 't': 'z',
    'u': 'x', 'v': 'c', 'w': 'v', 'x': 'b', 'y': 'n', 'z': 'm'
}

# Mapeo inverso para descifrar
mapeo_descifrado = {v: k for k, v in mapeo_cifrado.items()}

def cifrar(texto):
    resultado = ""
    for char in texto.lower():
        if char in mapeo_cifrado:
            resultado += mapeo_cifrado[char]
        else:
            resultado += char
    return resultado

def descifrar(texto):
    resultado = ""
    for char in texto.lower():
        if char in mapeo_descifrado:
            resultado += mapeo_descifrado[char]
        else:
            resultado += char
    return resultado

# Programa principal
modo = input("֎ ¿Quieres cifrar o descifrar? (c/d): ").strip().lower()

if modo == "c":
    frase_original = input("Escribe la frase que quieres cifrar: ")
    frase_cifrada = cifrar(frase_original)
    print("֎ Texto cifrado:", frase_cifrada)

elif modo == "d":
    frase_cifrada = input("Escribe la frase cifrada: ")
    frase_descifrada = descifrar(frase_cifrada)
    print("֎ Texto descifrado:", frase_descifrada)

else:
    print("Opción no válida. Usa 'c' para cifrar o 'd' para descifrar.")
