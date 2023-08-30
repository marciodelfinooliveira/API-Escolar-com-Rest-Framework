#Calcula a média aritimática de valores de uma lista indefinida
def calcula_media(lista: list) -> float | int:
    soma = 0
    for iterador in range(len(lista)):
         soma += lista[iterador]
    return soma/len(lista)

#Recebe as notas e adiciona na lista
def recebe_nota(lista: list) -> None:
    lista.append(float(input("Insira a Nota: ")))
    
lista_notas = []
while True:
    recebe_nota(lista_notas)
    continuar = input("\nDeseja Continuar ? (Qualquer tecla)(s): ")
    if continuar in ["s", "S"]:
        continue
    else:
        print(calcula_media(lista_notas))
        break

