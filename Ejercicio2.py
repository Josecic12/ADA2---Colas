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

class SistemaDeColas:
    def __init__(self):
        self.colas = {
            0: Cola(),  # Cola para servicio prioritario
            1: Cola(),  # Cambio de llantas
            2: Cola(),  # Cambio de aceite
            3: Cola()   # Servicio completo
        }
        self.contadores = {
            0: 1,
            1: 1,
            2: 1,
            3: 1
        }
        self.servicios = {
            0: "Servicio prioritario",
            1: "Cambio de llantas",
            2: "Cambio de aceite",
            3: "Servicio completo"
        }

    def llegada_cliente(self, numero_servicio):
        if numero_servicio in self.colas:
            numero_atencion = self.contadores[numero_servicio]
            self.colas[numero_servicio].enqueue(numero_atencion)
            print(f"Cliente con número {numero_atencion} agregado a la cola de {self.servicios[numero_servicio]}")
            print(f"Cola actual de {self.servicios[numero_servicio]}: {self.colas[numero_servicio].mostrar()}")
            self.contadores[numero_servicio] += 1
        else:
            print(f"Servicio {numero_servicio} no existe.")

    def atender_cliente(self, numero_servicio):
        if not self.colas[0].esta_vacia():  # Prioridad para la cola del servicio prioritario
            numero_atencion = self.colas[0].dequeue()
            print(f"Atendiendo al cliente PRIORITARIO con número {numero_atencion} de {self.servicios[0]}.")
            print(f"Cola restante de {self.servicios[0]}: {self.colas[0].mostrar()}")
        elif numero_servicio in self.colas:
            numero_atencion = self.colas[numero_servicio].dequeue()
            if numero_atencion is not None:
                print(f"Atendiendo al cliente con número {numero_atencion} de {self.servicios[numero_servicio]}")
                print(f"Cola restante de {self.servicios[numero_servicio]}: {self.colas[numero_servicio].mostrar()}")
            else:
                print(f"No hay clientes para atender en la cola de {self.servicios[numero_servicio]}.")
        else:
            print(f"Servicio {numero_servicio} no existe.")

    def mostrar_estado_colas(self):
        print("Estado actual de las colas:")
        for servicio, cola in self.colas.items():
            print(f"{self.servicios[servicio]}: {cola.mostrar()}")

def simulador():
    sistema = SistemaDeColas()

    while True:
        comando = input("Ingrese el comando (C para llegada, A para atender, o Q para salir): ").upper()

        if comando == 'Q':
            print("Saliendo del sistema.")
            sistema.mostrar_estado_colas()
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
