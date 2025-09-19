CLIENTE DE CORREO ELECTRÓNICO

1ER ENTREGA

Comenzamos creando cada una de las clases para lograr entender cómo relacionarlas. Antes realizamos el diagrama en Visual Paradigm. Lo pensamos como mensajería interna, por ahora con los usuarios creados sin tener que realizar un logueo.

Se implementan las cuatro clases principales: Servidor, Mensaje, Usuario y Carpetas. La clase Servidor nos permite almacenar los usuario registrados y poder mostrarlos por consola; //En un futuro se podría validar el destinatario//. La clase Mensaje contiene los datos que representan a un mensaje como lo son el remitente, el destinatario, el asunto y el contenido. Cada mensaje muestra un objeto con sus atributos. La clase Carpeta utiliza una lista para almacenar los mensajes y otro metodo para mostrarlos. Y por último la clase Usuario, gestiona las carpetas y permite enviar y recibir mensajes.

Evaluamos qué debía contener la clase de Servidor_Correo y si debería tener una función dónde se pregunte si hay correo recorriendo la lista. Más adelante se podría hacer discriminar a qué usuario le corresponde cada correo.

Por ahora habrá solo dos bandejas: enviados y recibidos.

La clase Servidor_Correo solo tendrá la función para mostrar los usuarios que contiene y guardar a los usuarios que se van registrando:

class Servidor:
def **init**(self):
self.usuarios = []

    def agregar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def mostrar_usuarios(self):
        print("Usuarios en el servidor")
        for u in self.usuarios:
            print(f"{u.nombre} ({u.correo})")

La clase Mensaje solo representa un mensaje individual con los atributos que se necesitan para enviar un email: Remitente, destinatario, asunto y contenido. Y tiene el método Mostrar() que imprime por consola esos atributos.

Luego en la clase Usuario tendremos el metodo enviar_mensaje() donde creamos un objeto Mensaje que lo almacenamos dentro de la variable mensaje. Desde ahí self.correo referirá al usuario que envía el mensaje y luego destinatario.correo a quién está dirigido.

Creamos la clase carpeta para que cada mensaje vaya a una lista vacía, pero en la clase usuario habría que modificar las listas vacías de cada bandeja para que en realidad cuando un mensaje le llega a un usuario vaya directamente a la bandeja de ese usuario, lo mismo cuando se envía un mensaje.

Cambiamos las listas vacías de la clase usuario:

class Usuario:
def **init**(self, nombre, correo):
self.nombre = nombre
self.correo = correo
self.bandeja_entrada = []
self.bandeja_salida = []

por un diccionario:

self.carpetas = {
"entrada": Carpeta("Bandeja de entrada"),
"enviados": Carpeta("Bandeja de enviados")
}

EJECUCIÓN DEL PROGRAMA

Primero creamos el servidor, luego creamos los usuarios y por último los agregamos al servidor.

servidor = Servidor()

lucas = Usuario("Lucas", "lucasvergara.f@gmail.com")
carla = Usuario("Carla", "carlabrizuela@gmail.com")

servidor.agregar_usuario(lucas)
servidor.agregar_usuario(carla)

Podemos mostrar los usuarios agregados con:

servidor.mostrar_usuarios()

A continuación enviamos el mensaje:

lucas.enviar_mensaje(carla, "Saludo", "Hola, Carla, ¿cómo estás?")

Mostramos la bandeja de entrada de Carla para confirmar que el correo llegó:

carla.mostrar_carpeta("entrada")
