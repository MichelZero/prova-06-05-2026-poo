texto = "casa"
resultado = ""
for i, letra in enumerate(texto):
    if i % 2 == 0:
        resultado += letra.upper()
    else:
        resultado += letra
print(resultado)
