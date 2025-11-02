class Carpeta:
    def __init__(self, nombre):
        self._nombre = nombre
        self._mensajes = []
        self._subcarpetas = []

    @property
    def nombre(self):
        return self._nombre
    
    #Este método agrega un mensaje:

    def agregar_mensaje(self, mensaje):
        self._mensajes.append(mensaje)
    
    #Este método agrega una subcarpeta:
    
    def agregar_subcarpeta(self, subcarpeta):
        self._subcarpetas.append(subcarpeta)
    
    #Este método muestra mensajes de la carpeta y de sus subcarpetas:

    def mostrar_mensajes(self):
        print(f"Carpeta: {self._nombre}")
        if not self._mensajes:
            print(f"La bandeja {self._nombre} está vacía.")
        else:
            for m in self._mensajes:
                m.mostrar()
        for sub in self._subcarpetas:
            sub.mostrar_mensajes()

    def buscar_mensajes(self, remitente=None, asunto=None, contenido=None, destinatario=None ):
        encontrados = []
        for m in self._mensajes:
            if (remitente is None or m.remitente == remitente) and \
            (asunto is None or m.asunto == asunto) \
                (contenido is None or m.contenido == contenido) \
                (destinatario is None or m.destinario == destinatario):
                encontrados.append(m)
        for sub in self._subcarpetas:
            encontrados.extend(sub.buscar_mensajes(remitente, asunto))
        return encontrados
    
    def mover_mensaje(self, mensaje, carpeta_destino):
        if mensaje in self._mensajes:
            self._mensajes.remove(mensaje)
            carpeta_destino.agregar_mensaje(mensaje)
            return True
        for sub in self._subcarpetas:
            if sub.mover_mensaje(mensaje, carpeta_destino):
                return True
        return False
    
    def mostrar_arbol(self, nivel=0):
        print("   " * nivel + f"- {self.nombre}")
        for sub in self._subcarpetas:
            sub.mostrar_arbol(nivel + 1)
        
