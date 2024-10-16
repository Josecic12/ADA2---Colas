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
        print(f"Cola A: {cola_a.mostrar()}")
        print(f"Cola B: {cola_b.mostrar()}")
        elemento_a = cola_a.dequeue()
        elemento_b = cola_b.dequeue()
        suma = elemento_a + elemento_b
        cola_resultado.enqueue(suma)
        print(f"Resultado parcial: {cola_resultado.mostrar()}")

    print(f"Cola A vacía: {cola_a.mostrar()}")
    print(f"Cola B vacía: {cola_b.mostrar()}")

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

cola_c = Cola()
cola_c.enqueue(9)
cola_c.enqueue(6)
cola_c.enqueue(11)
cola_c.enqueue(19)
cola_c.enqueue(15)

print(f"Cola C (resultado): {cola_c.mostrar()}")

print(f"Estado final de Cola A: {cola_a.mostrar()}")
print(f"Estado final de Cola B: {cola_b.mostrar()}")
