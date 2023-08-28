while True:
    
    numero = int(input("Insira o número: "))
    print(f"Sucessor: {numero+1}\nAntecessor: {numero-1}")
    
    continuar = input("Deseja Continuar ? (Qualquer tecla)(s): ")
    if continuar in ["s", "S"]:
        continue
    else:
        break