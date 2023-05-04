def mostra_linha(nucleo_interno: int, linha_interno: int):
    print("")
    print(end=" " * (nucleo_interno - linha_interno))
    contador_interno = 1
    while contador_interno < (2 * linha_interno):
        print(end="{}".format(contador_interno))
        contador_interno += 1


nucleo_externo = int(input("Informe o número que determinará as dimensões do losango (Inteiro, maior que 1): "))
linha_externo = 1  # contador
while linha_externo < nucleo_externo:
    mostra_linha(nucleo_externo, linha_externo)
    linha_externo += 1
while linha_externo > 0:
    mostra_linha(nucleo_externo, linha_externo)
    linha_externo -= 1
