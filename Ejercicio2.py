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

class SistemaDeColas:
    def __init__(self):
        self.colas = {
            1: Cola(),
            2: Cola(),
            3: Cola()
        }
        self.contadores = {
            1: 1,
            2: 1,
            3: 1
        }

    def llegada_cliente(self, numero_servicio):
        if numero_servicio in self.colas:
            numero_atencion = self.contadores[numero_servicio]
            self.colas[numero_servicio].enqueue(numero_atencion)
            print(f"Cliente con número {numero_atencion} agregado a la cola del servicio {numero_servicio}")
            self.contadores[numero_servicio] += 1
        else:
            print(f"Servicio {numero_servicio} no existe.")

    def atender_cliente(self, numero_servicio):
        if numero_servicio in self.colas:
            numero_atencion = self.colas[numero_servicio].dequeue()
            if numero_atencion is not None:
                print(f"Atendiendo al cliente con número {numero_atencion} del servicio {numero_servicio}")
            else:
                print(f"No hay clientes para atender en la cola del servicio {numero_servicio}.")
        else:
            print(f"Servicio {numero_servicio} no existe.")

def simulador():
    sistema = SistemaDeColas()

    while True:
        comando = input("Ingrese el comando (C para llegada, A para atender, o Q para salir): ").upper()

        if comando == 'Q':
            print("Saliendo del sistema.")
            break

        try:
            if comando.startswith("C"):
                numero_servicio = int(comando[1:])
                sistema.llegada_cliente(numero_servicio)

            elif comando.startswith("A"):
                numero_servicio = int(comando[1:])
                sistema.atender_cliente(numero_servicio)

            else:
                print("Comando no reconocido. Ingrese C seguido del número de servicio o A seguido del número de servicio.")

        except ValueError:
            print("Formato de comando incorrecto. Asegúrese de ingresar C o A seguido de un número de servicio.")

simulador()
