from servidor import Servidor
from usuario import Usuario
from carpeta import Carpeta
from mensaje import Mensaje


def menu_servidor(servidor):
    while True:
        print("\n--- Servidor de correo ---")
        print("Usuarios registrados:")
        servidor.mostrar_usuarios()
        print("\nOpciones:")
        print("1 - Enviar mensaje")
        print("2 - Buscar mensajes")
        print("3 - Mover mensajes")
        print("4 - Mostrar bandeja de entrada")
        print("5 - Mostrar enviados")
        print("0 - Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "0":
            print("Saliendo del servidor...")
            break
        
        elif opcion == "1":
            remitente_nombre = input("Ingrese nombre del remitente: ").strip()
            destinatario_nombre = input("Ingrese nombre del destinatario: ").strip()
            asunto = input("Asunto: ").strip()
            contenido = input("Contenido: ").strip()
            
            remitente = next((u for u in servidor._usuarios if u.nombre == remitente_nombre), None)
            destinatario = next((u for u in servidor._usuarios if u.nombre == destinatario_nombre), None)
            
            if not remitente or not destinatario:
                print("Remitente o destinatario no válido.")
            else:
                servidor.enviar_mensaje(remitente, destinatario, asunto, contenido)
                print("Mensaje enviado.")

        elif opcion == "2":
            usuario_nombre = input("Ingrese el nombre del usuario: ").strip()
            usuario = next((u for u in servidor._usuarios if u.nombre == usuario_nombre), None)
            if not usuario:
                print("Usuario no encontrado.")
                continue
            
            carpeta_nombre = input("Carpeta (entrada/enviados): ").strip()
            remitente = input("Filtrar por remitente (Enter para omitir): ").strip() or None
            asunto = input("Filtrar por asunto (Enter para omitir): ").strip() or None
            
            resultados = usuario.carpetas.get(carpeta_nombre).buscar_mensajes(remitente=remitente, asunto=asunto)
            if not resultados:
                print("No se encontraron mensajes.")
            else:
                print(f"\nSe encontraron {len(resultados)} mensajes:")
                for m in resultados:
                    m.mostrar()

        elif opcion == "3":
            usuario_nombre = input("Ingrese el nombre del usuario: ").strip()
            usuario = next((u for u in servidor._usuarios if u.nombre == usuario_nombre), None)
            if not usuario:
                print("Usuario no encontrado.")
                continue
            
            carpeta_origen = input("Carpeta de origen (entrada/enviados): ").strip()
            carpeta_destino = input("Carpeta destino (entrada/enviados): ").strip()
            
            carpeta_o = usuario.carpetas.get(carpeta_origen)
            carpeta_d = usuario.carpetas.get(carpeta_destino)
            
            if not carpeta_o or not carpeta_d:
                print("Carpeta de origen o destino inválida.")
                continue
            
            remitente = input("Filtrar por remitente (Enter para omitir): ").strip() or None
            asunto = input("Filtrar por asunto (Enter para omitir): ").strip() or None
            
            encontrados = carpeta_o.buscar_mensajes(remitente=remitente, asunto=asunto)
            if not encontrados:
                print("No se encontraron mensajes para mover.")
            else:
                for m in encontrados:
                    carpeta_o.mover_mensaje(m, carpeta_d)
                print(f"Se movieron {len(encontrados)} mensajes.")

        elif opcion == "4" or opcion == "5":
            usuario_nombre = input("Ingrese el nombre del usuario: ").strip()
            usuario = next((u for u in servidor._usuarios if u.nombre == usuario_nombre), None)
            if not usuario:
                print("Usuario no encontrado.")
                continue
            
            carpeta_nombre = "entrada" if opcion == "4" else "enviados"
            usuario.mostrar_carpeta(carpeta_nombre)

        else:
            print("Opción no válida. Intente de nuevo.")

# --- EJEMPLO DE USO ---
servidor = Servidor()
lucas = Usuario("Lucas", "lucasvergara.f@gmail.com")
carla = Usuario("Carla", "carlabrizuela@gmail.com")
servidor.agregar_usuario(lucas)
servidor.agregar_usuario(carla)

menu_servidor(servidor)


# Inicialización de usuarios y servidor
servidor = Servidor()
lucas = Usuario("Lucas", "lucasvergara.f@gmail.com")
carla = Usuario("Carla", "carlabrizuela@gmail.com")
servidor.agregar_usuario(lucas)
servidor.agregar_usuario(carla)

# Ejecutar 
menu_servidor(servidor)
