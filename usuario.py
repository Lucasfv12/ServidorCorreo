from carpeta import Carpeta

class Usuario:
    def __init__(self, nombre, correo):
        self._nombre = nombre
        self._correo = correo
        self._carpetas = {
            "entrada": Carpeta("Bandeja de entrada"),
            "enviados": Carpeta("Bandeja de enviados")
        }

    @property
    def nombre(self):
        return self._nombre
    
    @property
    def correo(self):
        return self._nombre
    
    @property
    def carpetas(self):
        return self._carpetas
       
    def mostrar_carpeta(self, tipo):
        if tipo in self._carpetas:
            self._carpetas[tipo].mostrar_mensajes()
        else:
            print(f"La carpeta {tipo} no existe")
    
    def mostrar_carpetas(self):
        print(f"\nCarpetas de {self._nombre}:")
        for nombre, carpeta in self._carpetas.items():
            print(f"- {nombre} ({len(carpeta._mensajes)} mensajes)")
 
