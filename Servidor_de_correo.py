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
        self.carpetas = {
            "entrada": Carpeta("Bandeja de entrada"),
            "enviados": Carpeta("Bandeja de enviados")
        }
    
    def enviar_mensaje(self, destinatario, asunto, contenido):
        mensaje = Mensaje(self.correo, destinatario.correo, asunto, contenido)
        self.carpetas["enviados"].agregar_mensaje(mensaje)
        destinatario.recibir_mensaje(mensaje)
    
    def recibir_mensaje(self, mensaje):
        self.carpetas["entrada"].agregar_mensaje(mensaje)
        
    def mostrar_carpeta(self, tipo):
        if tipo in self.carpetas:
            self.carpetas[tipo].mostrar_mensajes()
        else:
            print(f"La carpeta {tipo} no existe")
            
class Carpeta:
    def __init__(self, nombre):
        self.nombre = nombre
        self.mensajes = []
    
    def agregar_mensaje(self, mensaje):
        self.mensajes.append(mensaje)
        
    def mostrar_mensajes(self):
        print(f"Carpeta: {self.nombre}")
        for m in self.mensajes:
            m.mostrar()


    

        



