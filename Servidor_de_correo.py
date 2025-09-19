class Servidor:
    def __init__(self):
        self.usuarios = []
    
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f"Se agregó el usuario: {usuario.nombre}")
        print("-" * 35)

    def mostrar_usuarios(self):
        print("Usuarios en el servidor")
        for u in self.usuarios:
            print(f"{u.nombre} ({u.correo})")
            print("-" * 35)

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
        if not self.mensajes:
            print(f"La bandeja ")
        else:
            for m in self.mensajes:
                m.mostrar()


#EJECUCIÓN DEL PROGRAMA

#*Creamos el servidor*
servidor = Servidor()


#*Creamos los usuarios*
lucas = Usuario("Lucas", "lucasvergara.f@gmail.com")
carla = Usuario("Carla", "carlabrizuela@gmail.com")

#*Agregamos los usuarios al servidor*
servidor.agregar_usuario(lucas)
servidor.agregar_usuario(carla)

#*Mostramos que los usuarios están en el servidor*

servidor.mostrar_usuarios()

#*Enviamos un mensaje*

lucas.enviar_mensaje(carla, "Saludo", "Hola, Carla, ¿cómo estás?")

#*Mostramos Bandeja de entrada del usuario Carla*

carla.mostrar_carpeta("entrada")
carla.mostrar_carpeta("enviados")




