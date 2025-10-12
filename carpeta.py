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

    def buscar_mensajes(self, remitente=None, asunto=None):
        encontrados = []
        for m in self._mensajes:
            if (remitente is None or m.remitente == remitente) and \
           (asunto is None or m.asunto == asunto):
                encontrados.append(m)
        for sub in self._subcarpetas:
            encontrados.extend(sub.buscar_mensajes(remitente, asunto))
        return encontrados
