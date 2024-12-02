class Grafo:
    def __init__(self):
        self.grafo = {}
    
    def agregar_nodo(self, nodo):
        if nodo not in self.grafo:
            self.grafo[nodo] = []
    
    def agregar_arista(self, nodo1, nodo2):
        if nodo1 in self.grafo and nodo2 in self.grafo:
            self.grafo[nodo1].append(nodo2)
            self.grafo[nodo2].append(nodo1)
        else:
            print("Uno o ambos nodos no existen.")
    
    def mostrar_grafo(self):
        for nodo, conexiones in self.grafo.items():
            print(f"{nodo}: {', '.join(conexiones)}")
ciudades_grafo = Grafo()
ciudades = [
    
    
    "Manizales", "Pereira", "Armenia", "Chinchiná", "Villamaria", 
    "Palestina", "Neira", "La Virginia", "Dosquebradas", "Santa Rosa de Cabal",
    "Cartago", "Calarcá", "Ciscasia", "La Tebaida", "Montenegro"   
]

for ciudad in ciudades:
    
    ciudades_grafo.agregar_nodo(ciudad)

ciudades_grafo.agregar_arista("Manizales", "Neira")
ciudades_grafo.agregar_arista("Manizales", "Palestina")
ciudades_grafo.agregar_arista("Manizales", "Villamaria")
ciudades_grafo.agregar_arista("Manizales", "Chinchiná")
ciudades_grafo.agregar_arista("Manizales", "Santa Rosa de Cabal")
ciudades_grafo.agregar_arista("Manizales", "Dosquebradas")
ciudades_grafo.agregar_arista("Manizales", "Pereira")
ciudades_grafo.agregar_arista("Manizales", "Cartago")
ciudades_grafo.agregar_arista("Manizales", "Armenia")
ciudades_grafo.agregar_arista("Santa Rosa de Cabal", "Pereira")
ciudades_grafo.agregar_arista("Santa Rosa de Cabal", "Armenia")
ciudades_grafo.agregar_arista("Dosquebradas", "Armenia")
ciudades_grafo.agregar_arista("Dosquebradas", "Pereira")
ciudades_grafo.agregar_arista("Dosquebradas", "Cartago")
ciudades_grafo.agregar_arista("La Virginia", "Pereira")
ciudades_grafo.agregar_arista("La Virginia", "Cartago")
ciudades_grafo.agregar_arista("Pereira", "Cartago")
ciudades_grafo.agregar_arista("Pereira", "Ciscasia")
ciudades_grafo.agregar_arista("Armenia", "Ciscasia")
ciudades_grafo.agregar_arista("Armenia", "Calarcá")
ciudades_grafo.agregar_arista("Armenia", "La Tebaida")
ciudades_grafo.agregar_arista("Armenia", "Montenegro")

ciudades_grafo.mostrar_grafo()