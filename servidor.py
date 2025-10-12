from mensaje import Mensaje

class Servidor:
    def __init__(self):
        self._usuarios = []
    
    def agregar_usuario(self, usuario):
        if usuario in self._usuarios:
            raise ValueError(f"El usuario '{usuario.nombre}' ya está registrado.")
        self._usuarios.append(usuario)
        print(f"Se agregó el usuario: {usuario.nombre}")
        
    def mostrar_usuarios(self): 
        for u in self._usuarios:
            print(f"{u.nombre} ({u.correo})")

    def enviar_mensaje(self, remitente, destinatario, asunto, contenido):
        if remitente not in self._usuarios:
            raise ValueError(f"El remitente '{remitente.nombre}' no está registrado en el servidor.")
        if destinatario not in self._usuarios:
            raise ValueError(f"El destinatario '{destinatario.nombre}' no está registrado en el servidor.")
        mensaje = Mensaje(remitente.correo, destinatario.correo, asunto, contenido)
        remitente.carpetas["enviados"].agregar_mensaje(mensaje)
        self._recibir_mensaje(destinatario, mensaje)
    
    def _recibir_mensaje(self, usuario, mensaje):
        if "entrada" not in usuario.carpetas:
            raise ValueError(f"El usuario '{usuario.nombre}' no tiene bandeja de entrada.")
        usuario.carpetas["entrada"].agregar_mensaje(mensaje)
    
    def listar_mensajes(self, usuario, carpeta):
        usuario.mostrar_carpeta(carpeta)