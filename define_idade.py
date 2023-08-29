# A função verifica se tem mais ou menos de 18
def verifica_idade(num):
    if num < 18:
        return False
    return True

# Verifica se a pessoa está apta a emitir CNH
def verifica_habilitacao(num):
    if verifica_idade(num):
        return print("Pode Obter Carteira de Motorista !!")
    return print("Não pode obter carteira de motorista !!")

# Tenta executar caso a entrada seja um número, se não, uma mensagem de erro é retornada
try:
    idade=int(input("Digite sua idade: "))
except ValueError:
    raise ValueError("Você não digitou um número inteiro !!")

# Executa o Programa
verifica_habilitacao(idade)