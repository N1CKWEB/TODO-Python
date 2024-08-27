


 # Ejemplo de Herencia simple



class ListaSimple:
    
    def __init__(self,elementos) -> None:
        self._elementos=list(elementos)
    
    
    def agregar_nuevo_elemento(self,elemento):
        self._elementos.append(elemento)
    
    
    # Obtener un elemento de nuestra lista con un indice
    def __getitem__(self,indice):
        return self._elementos[indice]
      

    def ordenar(self):
     self._elementos.sort()   

   
    def __len__(self): 
        return len(self._elementos)
    
    
    def __repr__(self) -> str:
        return f"{self.__class__.__name__} [Elemento: {self._elementos!r} ]" 


class ListaOrdenada(ListaSimple):
    
    def __init__(self, elementos=[]) -> None:
        super().__init__(elementos)
        # Ordenamos siempre los elementos una vez inicializados
        self.ordenar()
        
    def agregar_nuevo_elemento(self, elemento):
        super().agregar_nuevo_elemento(elemento)
        self.ordenar()
    
    
class ListaEnteros(ListaSimple):
    
    def __init__(self, elementos=[]) -> None:
        for elemento in elementos:
            self._validar=elemento
        # Una vez validados los elementos los agregamos los atributos definidos en la clase padre
        super().__init__(elementos)
    
    def validar(self,elemento):
        #Validamos si el elementos es de tipo entero
        if not isinstance(elemento,int):
            raise ValueError(f'No es valor entero: {elemento}')
        
    # Sobreescribir el método validar
    def agregar_nuevo_elemento(self, elemento):
        self._validar(elemento)
        # Una vez validado lo agregamos a la lista
        super().agregar_nuevo_elemento(elemento) 
         
lista01=ListaSimple([4,2,6,8,9])
print(lista01)

lista01.agregar_nuevo_elemento(23)

print(lista01)

lista01.ordenar()

print(lista01)

lista_ordenada=ListaOrdenada([23,1,5,7,9,33,28])

print(lista_ordenada)

lista_ordenada.agregar_nuevo_elemento(-12)

print(lista_ordenada)

print(len(lista01))
print(len(lista_ordenada))

# Lista de enteros

lista_de_enteros=ListaEnteros([1,23,56,44,688,42,-12])
print(lista_de_enteros)
