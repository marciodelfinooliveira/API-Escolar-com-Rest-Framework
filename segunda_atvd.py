try:  
    continuar='s'
    while continuar in ["s", "S"]:    
        numero = round(float(input("Insira o número: ")))
        print(f"\nSucessor de {numero}: {numero+1}\nAntecessor de {numero}: {numero-1}")
    
        continuar = input("\nDeseja Continuar ? (Não = Qualquer tecla)(Sim = s): ")
         
except ValueError:
    raise ValueError("Você não digitou um número !!")