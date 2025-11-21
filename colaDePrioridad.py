class Nodo:
    def __init__(self, prioridad, mensaje):
        self.prioridad = prioridad
        self.mensaje = mensaje
        self.siguiente = None


class ColaDePrioridad:
    def __init__(self):
        self.frente = None

    def encolar(self, prioridad, mensaje):
        nuevo = Nodo(prioridad, mensaje)

        # Si está vacía o el nuevo tiene prioridad más alta (menor número)
        if not self.frente or prioridad < self.frente.prioridad:
            nuevo.siguiente = self.frente
            self.frente = nuevo
        else:
            actual = self.frente
            while actual.siguiente and actual.siguiente.prioridad <= prioridad:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo

    def desencolar(self):
        if not self.frente:
            return None
        nodo = self.frente
        self.frente = self.frente.siguiente
        return nodo.mensaje

    def esta_vacia(self):
        return self.frente is None

    def __iter__(self):  # Para poder recorrerla en el método buscar
        actual = self.frente
        while actual:
            yield actual.mensaje
            actual = actual.siguiente
