while True:    
    numero = int(input("Insira o número: "))
    print(f"\nSucessor: {numero+1}\nAntecessor: {numero-1}")
    
    continuar = input("\nDeseja Continuar ? (Não = Qualquer tecla)(Sim = s): \n")
    if continuar in ["s", "S"]:
        continue
    else:
        break