from servidor import Servidor
from usuario import Usuario
from carpeta import Carpeta
from mensaje import Mensaje


def menu_servidor(servidor):
    while True:
        print("\n--- Servidor de correo ---")
        print("El servidor de correo cuenta con los siguientes usuarios:")
        servidor.mostrar_usuarios()
        print("\nOpciones:")
        print("1 - Enviar mensaje")
        print("2 - Buscar mensajes")
        print("3 - Mover mensajes")
        print("4 - Mostrar bandeja de entrada")
        print("5 - Mostrar bandeja de enviados")
        print("6 - Mostrar todas las carpetas del usuario")
        print("0 - Salir")
        
        opcion = input("Seleccione una opción: ").strip()
        
        if opcion == "0":
            print("Saliendo del servidor...")
            break

        # ----- ENVIAR MENSAJE -----
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

        # ----- BUSCAR MENSAJES -----
        elif opcion == "2":
            usuario_nombre = input("Ingrese el nombre del usuario: ").strip()
            usuario = next((u for u in servidor._usuarios if u.nombre == usuario_nombre), None)

            if not usuario:
                print("Usuario no encontrado.")
                continue
            
            carpeta_nombre = input("Carpeta (entrada/enviados/otras): ").strip().lower()
            carpeta = usuario.carpetas.get(carpeta_nombre)
            
            if not carpeta:
                print(f"La carpeta '{carpeta_nombre}' no existe.")
                continue

            remitente = input("Filtrar por remitente (Enter para omitir): ").strip() or None
            asunto = input("Filtrar por asunto (Enter para omitir): ").strip() or None
            
            resultados = carpeta.buscar_mensajes(remitente=remitente, asunto=asunto)

            if not resultados:
                print("No se encontraron mensajes.")
            else:
                print(f"\nSe encontraron {len(resultados)} mensajes:")
                for m in resultados:
                    m.mostrar()

        # ----- MOVER MENSAJES -----
        elif opcion == "3":
            usuario_nombre = input("Usuario: ").strip()
            usuario = next((u for u in servidor._usuarios if u.nombre == usuario_nombre), None)

            if not usuario:
                print("Usuario no encontrado.")
                continue
            
            carpeta_origen_nombre = input("Carpeta origen (entrada/enviados): ").strip().lower()
            carpeta_o = usuario.carpetas.get(carpeta_origen_nombre)

            if not carpeta_o:
                print("Carpeta de origen inválida.")
                continue

            # Mostrar mensajes disponibles para elegir
            if not carpeta_o._mensajes:
                print("No hay mensajes en esta carpeta.")
                continue

            print("\nMensajes disponibles:")
            for i, m in enumerate(carpeta_o._mensajes):
                print(f"{i} - Asunto: {m.asunto} | Remitente: {m.remitente}")

            idx = int(input("Seleccione el índice del mensaje a mover: "))
            mensaje = carpeta_o._mensajes[idx]

            # Mostrar carpetas disponibles
            print("\nCarpetas disponibles para mover el mensaje:")
            for c in usuario.carpetas.keys():
                print(f"- {c}")

            carpeta_destino_nombre = input("Seleccione carpeta destino o escriba un nuevo nombre: ").strip().lower()
            carpeta_d = usuario.carpetas.get(carpeta_destino_nombre)

            # Si la carpeta destino no existe, preguntar si crearla
            if not carpeta_d:
                crear = input(f"La carpeta '{carpeta_destino_nombre}' no existe. ¿Desea crearla? (s/n): ").lower()
                if crear == "s":
                    carpeta_d = Carpeta(carpeta_destino_nombre)
                    usuario.carpetas[carpeta_destino_nombre] = carpeta_d
                    print(f"Carpeta '{carpeta_destino_nombre}' creada correctamente.")
                else:
                    print("Operación cancelada.")
                    continue

            # Mover mensaje
            carpeta_o.mover_mensaje(mensaje, carpeta_d)
            print("Mensaje movido correctamente.")

        # ----- MOSTRAR CARPETAS -----
        elif opcion == "4" or opcion == "5":
            usuario_nombre = input("Ingrese el nombre del usuario: ").strip()
            usuario = next((u for u in servidor._usuarios if u.nombre == usuario_nombre), None)

            if not usuario:
                print("Usuario no encontrado.")
                continue
            
            carpeta_nombre = "entrada" if opcion == "4" else "enviados"
            usuario.mostrar_carpeta(carpeta_nombre)

        # ----- MOSTRAR TODAS LAS CARPETAS -----
        elif opcion == "6":
            usuario_nombre = input("Ingrese el nombre del usuario: ").strip()
            usuario = next((u for u in servidor._usuarios if u.nombre == usuario_nombre), None)

            if not usuario:
                print("Usuario no encontrado.")
                continue

            # Mostrar solo nombre y cantidad de mensajes sin repetir
            print(f"\nCarpetas de {usuario.nombre}:")
            for nombre, carpeta in usuario.carpetas.items():
                print(f"- {nombre} ({len(carpeta._mensajes)} mensajes)")

        else:
            print("Opción no válida. Intente de nuevo.")


# --- EJEMPLO DE USO ---
servidor = Servidor()
lucas = Usuario("Lucas", "lucasvergara.f@gmail.com")
carla = Usuario("Carla", "carlabrizuela@gmail.com")
servidor.agregar_usuario(lucas)
servidor.agregar_usuario(carla)

menu_servidor(servidor)





