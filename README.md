ESTRUCTURAS DE DATOS
Profesor: Leonardo Bianco.

Proyecto Final: CLIENTE DE CORREO ELECTRÓNICO

1ER ENTREGA

INTEGRANTES:
*Brizuela, Carla.
*Vergara, Lucas.

Comenzamos creando cada una de las clases para lograr entender cómo relacionarlas. Antes realizamos el diagrama en Visual Paradigm. Lo pensamos como mensajería interna, por ahora con los usuarios creados sin tener que realizar un logueo.

Se implementan las cuatro clases principales: Servidor, Mensaje, Usuario y Carpetas. La clase Servidor nos permite almacenar los usuario registrados y poder mostrarlos por consola; //En un futuro se podría validar el destinatario//. La clase Mensaje contiene los datos que representan a un mensaje como lo son el remitente, el destinatario, el asunto y el contenido. Cada mensaje muestra un objeto con sus atributos. La clase Carpeta utiliza una lista para almacenar los mensajes y otro metodo para mostrarlos. Y por último la clase Usuario, gestiona las carpetas y permite enviar y recibir mensajes.

Evaluamos qué debía contener la clase de Servidor_Correo y si debería tener una función dónde se pregunte si hay correo recorriendo la lista. Más adelante se podría hacer discriminar a qué usuario le corresponde cada correo.

Por ahora habrá solo dos bandejas: enviados y recibidos.

La clase Servidor_Correo solo tendrá la función para mostrar los usuarios que contiene y guardar a los usuarios que se van registrando:

class Servidor:
def _init_(self):
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
def _init_(self, nombre, correo):
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

También podemos mostrar la bandeja de enviados de Lucas con:

lucas.mostrar_carpeta("enviados")



***************************************
*     3RA ENTREGA - REORGANIZACIÓN    *
***************************************

1) Agregamos una interfaz de Linea de comando para reorganizar el archivo main.py. El nuevo MAIN se gestiona a través de la función menu_servidor, respondiendo a la necesidad de construir un sistema más usable mediante la ejecución de comandos que aseguren que todos los componentes operen según lo esperado. La sección anterior contaba con una serie de comandos ejecutados secuencialmente sin necesidad de la interacción con el usuario. 

2) En el archivo carpeta.py se modifica el método buscar_mensaje debido a que el mismo solo realizaba la busqueda de mensajes a partir de remitente y el asunto. Entendemos que la busqueda en ese caso un poco acotada y agregamos la busqueda por contenido y asunto. También comprendemos que el hecho de busqueda por remitente es obvio, debido a que el usuario no realiza el filtro de busqueda buscando mensaje de sí mismo porque la casilla de correo le corresponde a él mismo, pero en nuestro caso podemos permitirnos esa busqueda ya que disponemos de dos usuarios en el servidor. 

3) Agregamos el método mover_mensaje. De esta manera, el usuario primero debe buscar el mensaje con el metodo de busquedad de mensaje y luego utilizar el metodo mover_mensaje que recorre recursivamente las carpetas y subcarpetas, lo elimina de la carpeta donde se encuentra y lo agrega en la carpeta destino.

4) Al agregar el método mover_mensaje y querer mover un mensaje de una carpeta a otra, por ejemplo moverlo desde la bandeja de entrada a spam, nos arrojaba el error: INDEXerror: list index out of range. Debido a que la carpeta spam no existía. De esta manera probamos como solución: si el usuario escribe una carpeta destino, y la carpeta existe, la movemos, si no existe, el CLI pregunta si quiere crearla, respondiendo por sí o por no. Luego se mueve el mensaje a la carpeta creada.

5) De la misma manera el método mover_mensaje y la implementación del CLI nos trajo otros inconvenientes. Uno de ellos es que no podíamos aprovechar en su totalidad la recursividad. No estabamos pudiendo navegar entre subcarpetas y no teniamos el acceso a la carpetas del usuario en el menú. Entonces agregamos la opción "Mostrar todas las carpetas del usuario". No sabemos con exactitud si es la mejor decisión. Es verdad que una interfaz gráfica sería de mayor utilidad en este caso que la línea de comandos, pero al mismo tiempo todavía más compleja. Pensamos también en la opción "Buscar carpeta", pero el usuario debería recordar las carpetas y el nombre de cada una de ellas y no nos parecía operativo. 

6) Solucionamos el error que arrojaba al buscar los mensajes por medio del CLI, como antes la utilización de los métodos era manual, no arrojaba el error si no indicábamos el filtro del mensaje que estábamos buscando. Al agregarle el CLI el error aparece ya que no teníamos una excepción en el caso de que la el destinatario no existe, el remitente o alguno de los datos solicitados. De esta manera, ahora se verifica primero si la carpeta existe antes de llamar a buscar_mensaje y se evita el error.