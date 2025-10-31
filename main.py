

#EJECUCIÓN DEL PROGRAMA

print()
servidor = Servidor()
print("El servidor de correo se ha sido inicializado")
print("------------------------------------------")

print("Los siguientes Usuarios se han agregado en el servidor:")
print()
lucas = Usuario("Lucas", "lucasvergara.f@gmail.com")
carla = Usuario("Carla", "carlabrizuela@gmail.com")

servidor.agregar_usuario(lucas)
servidor.agregar_usuario(carla)

#Mostramos los usuarios:

servidor.mostrar_usuarios()
print("-------------------")

#Creamos la subcarpeta Spam dentro de la bandeja de entrada:
spam_lucas = Carpeta("Spam")
lucas.carpetas["entrada"].agregar_subcarpeta(spam_lucas)

spam_carla = Carpeta("Spam")
carla.carpetas["entrada"].agregar_subcarpeta(spam_carla)

#Enviamos mensajes:

print("El usuario Lucas está enviando un mensaje...\n")
servidor.enviar_mensaje(lucas, carla, "Saludo", "Hola, Carla, ¿cómo estás?")

print("Carla responde...\n")
servidor.enviar_mensaje(carla, lucas, "Tanto tiempo!", "Hola Lucas, ¿cómo estás, tanto tiempo?")

#Agregamos un mensaje de Spam
print("\n")
spam_lucas.agregar_mensaje(Mensaje("carla", "lucas", "Oferta", "Oferta de celulares Samsung"))

#Muestra la bandeja de entrada de Carla
print("\nBandeja de entrada de Carla:")
entrada_carla = carla.carpetas["entrada"]
entrada_carla.mostrar_mensajes()

#Muestra la bandeja de entrada de Lucas
print("\nBandeja de entrada de Lucas:")
entrada_lucas = lucas.carpetas["entrada"]
entrada_lucas.mostrar_mensajes()

#Muestra bandeja de enviados de Lucas
print("\nBandeja de enviados de Lucas:")
enviados_lucas = lucas.carpetas["enviados"]
enviados_lucas.mostrar_mensajes()

#Busqueda recursiva en la carpeta de entrada de Lucas
print("\nBúsqueda de mensajes en la carpeta de entrada de Lucas:")
busqueda = entrada_lucas.buscar_mensajes(remitente="carla")
for m in busqueda:
    m.mostrar()

#Busqueda del mensaje "Saludos" en la bandeja de entrada de Carla
print("\nBúsqueda de mensajes con asunto 'Saludo' en la carpeta de entrada de Carla:")
busqueda2 = entrada_carla.buscar_mensajes(asunto="Saludo")
for m in busqueda2:
    m.mostrar()

# Búsqueda recursiva: mensajes con asunto 'Oferta' en la carpeta Spam de Lucas
print("\nBúsqueda de mensajes con asunto oferta:")
resultados3 = entrada_lucas.buscar_mensajes(asunto="Oferta")
for m in resultados3:
    m.mostrar()