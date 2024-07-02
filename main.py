import os

#Lista Contacto
## VARIABLES GLOBALES
lista_contactos = []

# Mostrar Menu
def display_menu():
    print("""Menu Contactos

    1- Crear Contacto
    2- Mostrar Contactos
    3- Eliminar Contacto
    4- Actualizar
    5- Salir     
    """)

def mostrar_contactos():
    index = 0
    for contacto in lista_contactos:
        print(f"{index} - {contacto}")
        index += 1


# contacto = {
#     "nombre": "Fernando",
#     "telefono": 1232132,
#     "email": "NA",
# }

#Nuestra aplicacion
def main():
    global lista_contactos

    while True:
        display_menu()  
        choice = input("\nElige una opcion para hacer: ")
        #if
        match choice:
            #elif
            case "1":
                nombre = input("Ingresa el nombre del contacto: ")
                telefono = input("Ingresa el telefono del contacto: ")
                email = input("Ingresa el email del contacto: ")

                contacto = {
                    "nombre": nombre,
                    "telefono": telefono,
                    "email": email,
                }
                lista_contactos.append(contacto)
                print(lista_contactos)
                input("Apreta Enter para continuar")
                #ESTE COMANDO LIMPIA LA TERMINAL
                os.system("clear")
            #elif
            case "2":
                mostrar_contactos()
                input("Apreta Enter para continuar")
                os.system("clear")
            case "3":
                try:
                    mostrar_contactos()
                    choice = int(input("Que contacto quieres eliminar: "))
                    contacto_eliminado = lista_contactos.pop(choice)
                    print(f"El contacto eliminado es: {contacto_eliminado}")
                except ValueError:
                    print("Ingresa un numero entero")
                except IndexError:
                    print("El numero tiene que corresponder con el ID del contacto existente")
                except:
                    print("Ha ocurrido un error")
                input("Apreta Enter para continuar")
                os.system("clear")
            case "4":
                print("Actualizar Contacto")
                input("Apreta Enter para continuar")
                os.system("clear")
            case "5":
                print("Adios!")
                break
            case _:
                print("Ingresa una opcion valida")
                input("Apreta Enter para continuar")
                os.system("clear")
        # if choice == "1":
        #     print("Crear Contacto")
        # elif choice == "2":
        #     print("Crear Contacto")
        # elif choice == "3":
        #     print("Crear Contacto")
        # elif choice == "4":
        #     print("Crear Contacto")
        # elif choice == "5":
        #     break
        # else:
        #     print("Ingresa una opcion correcta\n")

main()