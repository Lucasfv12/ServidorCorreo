class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido):
        self.remitente = remitente
        self.destinatario = destinatario
        self.asunto = asunto
        self.contenido = contenido

    def mostrar(self):
        print(f"De: {self.remitente}")
        print(f"Para: {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Contenido: {self.contenido}")

class Carpeta:
    def __init__(self, bandeja_entrada, bandeja_salida):
        self.bandeja_entrada = bandeja_entrada
        self.bandeja_salidad = bandeja_salida

class Servidor:
    def __init__(self, usuarios):
        self.usuarios = []
    
    def agregar_usuario():
        usuario = Usuario(self.nombre, self.correo)
        


class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.bandeja_recibidos = []
        self.bandeja_enviados = []

    # INTERFAZ: ENVIAR MENSAJE
    def enviar_mensaje(self, destinatario, asunto, contenido):
        mensaje = Mensaje(self.correo, destinatario.correo, asunto, contenido)
        self.bandeja_enviados.append(mensaje)  # lo guardo en enviados
        destinatario.recibir_mensaje(mensaje)  # se lo envío al destinatario

    # INTERFAZ: RECIBIR MENSAJE
    def recibir_mensaje(self, mensaje):
        self.bandeja_recibidos.append(mensaje)

    # INTERFAZ: LISTAR BANDA DE ENTRADA
    def mostrar_bandeja_entrada(self):
        print(f"\nBandeja de entrada de {self.nombre}:")
        if not self.bandeja_recibidos:
            print("No hay mensajes.")
        for m in self.bandeja_recibidos:
            m.mostrar()

    # INTERFAZ: LISTAR BANDA DE SALIDA
    def mostrar_bandeja_salida(self):
        print(f"\nBandeja de salida de {self.nombre}:")
        if not self.bandeja_enviados:
            print("No hay mensajes enviados.")
        for m in self.bandeja_enviados:
            m.mostrar()


# ------------------- EJEMPLO DE USO -------------------

# Crear usuarios
lucas = Usuario("Lucas", "lucas@correo.com")
carla = Usuario("Carla", "carla@correo.com")

# # Lucas envía mensaje a Carla
# lucas.enviar_mensaje(carla, "Reunión", "Nos vemos mañana")

# Mostrar bandejas
lucas.mostrar_bandeja_salida()
carla.mostrar_bandeja_entrada()
