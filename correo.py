# class Casa:
#      def __init__(self, color, habitaciones):
#          self.color = color
#          self.habitaciones = habitaciones
    
#      def pintar(self, nuevo_color):
#          self.color = nuevo_color

# mi_casa = Casa("roja", 3)

# print("El color inicial de la casa es: ", mi_casa.color)

# mi_casa.pintar("verde")

#print("Ahora pinté la casa y es de color: ", mi_casa.color)

class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido ):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido

    def mostrar(self):
        print(f"De: {self.remitente}")
        print(f"Para: {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Contenido: {self.contenido}")

# mensaje = Mensaje("lucas@correo.com", "carla@correo.ar", "correo", "Hola Carla")
# print("De: ", mensaje.remitente)

# mensaje1 = Mensaje("lucasvergara.f@ondadinamita.com", "carlabrizuela@escuadronlobo.com", "Reunión", "Nos vemos mañana")
# mensaje1.mostrar()

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.bandeja_recibidos = []
        self.bandeja_enviados = []

    def enviar_mensaje(self, destinatario, asunto, contenido):
        mensaje = Mensaje(self.correo, destinatario.correo, asunto, contenido)
        self.bandeja_enviados.append(mensaje)
        
    def recibir_mensaje(self, mensaje):
        self.bandeja_recibidos.append(mensaje)

    def mostrar_bandeja_entrada(self):
        print(f"Bandeja de {self.nombre}:")
        for m in self.bandeja_recibidos:
            m.mostrar()

#     def recibir_mensaje(self, mensaje):
#         self.recibidos.append(mensaje)










