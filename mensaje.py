class Mensaje:
    def __init__(self, remitente, destinatario, asunto, contenido):
        self._remitente = remitente
        self._destinatario = destinatario
        self._asunto = asunto
        self._contenido = contenido
    
    @property
    def remitente(self):
        return self._remitente

    @property
    def destinatario(self):
        return self._destinatario

    @property
    def asunto(self):
        return self._asunto

    @property
    def contenido(self):
        return self._contenido

    def mostrar(self):
        print(f"De: {self.remitente}")
        print(f"Para: {self.destinatario}")
        print(f"Asunto: {self.asunto}")
        print(f"Contenido: {self.contenido}")
    
    def __str__(self):
        return f"De: {self.remitente}\nPara: {self.destinatario}\nAsunto: {self.asunto}\nContenido: {self.contenido}"