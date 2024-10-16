class Cola:
    def __init__(self):
        self.items = []

    def esta_vacia(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.esta_vacia():
            return self.items.pop(0)
        else:
            return None

    def tamano(self):
        return len(self.items)

    def mostrar(self):
        return self.items

def sumar_colas(cola_a, cola_b):
    cola_resultado = Cola()

    while not cola_a.esta_vacia() and not cola_b.esta_vacia():
        elemento_a = cola_a.dequeue()
        elemento_b = cola_b.dequeue()
        suma = elemento_a + elemento_b
        cola_resultado.enqueue(suma)

    return cola_resultado

cola_a = Cola()
cola_b = Cola()

cola_a.enqueue(3)
cola_a.enqueue(4)
cola_a.enqueue(2)
cola_a.enqueue(8)
cola_a.enqueue(12)

cola_b.enqueue(6)
cola_b.enqueue(2)
cola_b.enqueue(9)
cola_b.enqueue(11)
cola_b.enqueue(3)

cola_resultado = sumar_colas(cola_a, cola_b)

print(cola_resultado.mostrar())
