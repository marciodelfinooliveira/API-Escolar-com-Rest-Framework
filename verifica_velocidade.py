# A função verifica se a velocidade foi acima da permitida
def verifica_velocidade(num):
    if num <= 80:
        return False
    return True

# Calcula o valor da multa
def calcula_multa(num):return num*7

# Verifica se o veiculo será multado e imprime na tela
def verifica_multa(num):
    if verifica_velocidade(num):
        return print(f"Você cruzou o radar a {num}km/h e está sendo "+
                     f"multado em R$ {calcula_multa(num)},00 reais")
    return print("Velocidade dentro da esperada.")
    
# Tenta executar caso a entrada seja um número, se não, uma mensagem de erro é retornada
try:
    velocidade=int(input("Velocidade no radar: "))
except ValueError:
    raise ValueError("Você não digitou um número inteiro !!")

# Executa o Programa
verifica_multa(velocidade)
