from colaDePrioridad import ColaDePrioridad

class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []
        self._subcarpetas = []
        self._urgentes = ColaDePrioridad()

    @property
    def nombre(self):
        return self._nombre
    
    #Este método agrega una subcarpeta:
    
    def agregar_subcarpeta(self, subcarpeta):
        self._subcarpetas.append(subcarpeta)
    
    #Este método muestra mensajes de la carpeta y de sus subcarpetas:

    def mostrar_mensajes(self):
        print(f"Carpeta: {self._nombre}")
        if not self._mensajes and self._urgentes.esta_vacia():
            print(f"La bandeja {self._nombre} está vacía.")
            return
        
        #Mostrar los urgentes primeros
        print("\n MENSAJES URGENTES ")
        temp = []
        while not self._urgentes.esta_vacia():
            m = self._urgentes.desencolar()
            m.mostrar()
            temp.append((0, m))
        #Devolverlos a la cola
        for _, m in temp:
            self._urgentes.encolar(0, m)
            
        #Mostrar los mensajes normales
        print("\n MENSAJE NORMALES ")
        for m in self._mensajes:
            m.mostrar()

    def buscar_mensajes(self, remitente=None, asunto=None, contenido=None, destinatario=None ):
        encontrados = []

        #BUSCA EN LOS MENSAJES COMUNES
        for m in self._mensajes:
            if (remitente is None or m.remitente == remitente) and \
            (asunto is None or m.asunto == asunto) and \
                (contenido is None or m.contenido == contenido) and \
                (destinatario is None or m.destinatario == destinatario):
                encontrados.append(m)

        #BUSCA EN LOS MENSAJES URGENTES:
        for m in self._urgentes:
           if (remitente is None or m.remitente == remitente) and \
              (asunto is None or m.asunto == asunto) and \
              (contenido is None or m.contenido == contenido) and \
              (destinatario is None or m.destinatario == destinatario):
               encontrados.append(m)

        #BUSCAR RECURSIVAMENTE EN LAS SUBCARPETAS
        for sub in self._subcarpetas:
            encontrados.extend(sub.buscar_mensajes(remitente, asunto, contenido, destinatario))
        return encontrados
    
    def mover_mensaje(self, mensaje, carpeta_destino):

        #MOVER LOS MENSAJES NORMALES
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)
            return True
        
        #MOVER MENSAJES URGENTES

        temp = []
        movido = False
        while not self._urgentes.esta_vacia():
            m = self._urgentes.desencolar()
            if m == mensaje:
                carpeta_destino.agregar_mensaje(mensaje)
                movido = True
            else:
                temp.append(m)
        for m in temp:
            self._urgentes.encolar(0, m)
        if movido:
            return True
        
        #BUSCAR EN SUBCARPETAS  
        for sub in self._subcarpetas:
            if sub.mover_mensaje(mensaje, carpeta_destino):
                return True
        return False
    
    def obtener_mensajes(self):
        return self._mensajes
    
    def agregar_mensaje(self, mensaje):
        if mensaje.urgente:
            self._urgentes.encolar(0, mensaje)
        else:
            self._mensajes.append(mensaje)


    def mostrar_arbol(self, nivel=0):
        print("   " * nivel + f"- {self.nombre}")
        for sub in self._subcarpetas:
            sub.mostrar_arbol(nivel + 1)
        
