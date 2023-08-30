from abc import ABC, abstractmethod

class Animal(ABC):
        
    def falando(self):
        '''defina na classe filha'''
        
    def andando(self):
        '''defina na classe filha'''

class Doguinho(Animal):

    def __init__(self, voz, patas) -> None:
        self.voz = voz
        self.patas = patas
    
    def falando(self):
        return self.voz
    
    def andando(self):
        return self.patas
        
class Pessoa:
    
    def __init__(self, nome, idade) -> None:
        self.__nome = nome
        self.idade = idade
        self.__humano = True
        
dog = Doguinho("Auauauau", 4)
joao = Pessoa("Joao Davi", 45)

print(dog.andando())
print(dog.falando())
print(joao.idade)
print()