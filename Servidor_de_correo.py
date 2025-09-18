class Servidor:
    def __init__(self):
        self.usuarios = []
    
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_usuarios(self):
        print("Usuarios en el servidor")
        for u in self.usuarios:
            print(f"{u.nombre} ({u.correo})")

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

class Usuario:
    def __init__(self, nombre, correo):
        self.nombre = nombre
        self.correo = correo
        self.bandeja_entrada = []
        self.bandeja_salida = []
    
    def enviar_mensaje(self, destinatario, asunto, contenido):
        mensaje = Mensaje(self.correo, destinatario.correo, asunto, contenido)
        destinatario.recibir_mensaje(mensaje)


    

        



