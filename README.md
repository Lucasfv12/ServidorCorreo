CLIENTE DE CORREO ELECTRÓNICO

1ER ENTREGA

Comenzamos creando cada una de las clases para lograr entender cómo relacionarlas. Antes realizamos el diagrama en Visual Paradigm. Lo pensamos como mensajería interna, por ahora con los usuarios creados sin tener que realizar un logueo.

Evaluamos qué debía contener la clase de Servidor_Correo y si debería tener una función dónde se pregunte si hay correo recorriendo la lista. Más adelante se podría hacer discriminar a qué usuario le corresponde cada correo.

Por ahora habrá solo dos bandejas: enviados y recibidos.

La clase Servidor_Correo solo tendrá la función para mostrar los usuarios que contiene y guardar a los usuarios que se van registrando:

class Servidor:
    def __init__(self):
        self.usuarios = []
    
    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_usuarios(self):
        print("Usuarios en el servidor")
        for u in self.usuarios:
            print(f"{u.nombre} ({u.correo})")

La clase Mensaje solo representa un mensaje individual con los atributos que se necesitan para enviar un email: Remitente, destinatario, asunto y contenido. Y tiene el método Mostrar() que imprime por consola esos atributos.

Luego en la clase Usuario tendremos el metodo enviar_mensaje() donde creamos un objeto Mensaje que lo almacenamos dentro de la variable mensaje. Desde ahí self.correo referirá al usuario que envía el mensaje y luego destinatario.correo a quién está dirigido.
