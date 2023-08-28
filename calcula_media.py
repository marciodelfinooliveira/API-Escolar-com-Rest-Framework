#Calcula a média de valores de uma lista indefinida
def calcula_media(lista):
    soma = 0
    for iterador in range(len(lista)):
         soma += lista[iterador]
    return soma/len(lista)

#Recebe as notas e adiciona na lista
def recebe_nota(lista):
    lista_notas.append(float(input("Insira a Nota: ")))
    
lista_notas = []
while True:
    recebe_nota(lista_notas)
    continuar = input("Deseja Continuar ? (Qualquer tecla)(s): ")
    if continuar in ["s", "S"]:
        continue
    else:
        print(calcula_media(lista_notas))
        break

