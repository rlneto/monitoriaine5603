def mostraLinha(nucleo_losango: int, linha: int):
    print("")
    print(end=" " * (nucleo_losango - linha))
    contador = 1
    while contador < (2 * linha):
        print(end="{}".format(contador))
        contador += 1


nucleo = int(input("Informe o número que determinará as dimensões do losango (Inteiro, maior que 1): "))
contador_externo = 1
while contador_externo < nucleo:
    mostraLinha(nucleo, contador_externo)
    contador_externo += 1
while contador_externo > 0:
    mostraLinha(nucleo, contador_externo)
    contador_externo -= 1
