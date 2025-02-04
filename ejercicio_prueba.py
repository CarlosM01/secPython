import sqlite3
import getpass

try:
    #Crear base de datos
    con = sqlite3.connect("ejercicio.db")
    con.execute("PRAGMA foreign_keys = ON")
    cur = con.cursor()


    #Crear tablas
    cur.execute('''
        CREATE TABLE IF NOT EXISTS usuarios(
            id_usuario INTEGER PRIMARY KEY,
            nickName TEXT NOT NULL UNIQUE,
            password TEXT NOT NULL,
            nombre_usuario TEXT NOT NULL,
            apellido_usuario TEXT NOT NULL,
            email_usuario TEXT NOT NULL
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS tipo_cliente(
            id_type INTEGER PRIMARY KEY,
            tipo_cliente TEXT
        )
    ''')

    cur.execute('''
        CREATE TABLE IF NOT EXISTS clientes(
            id_cliente INTEGER PRIMARY KEY,
            run TEXT NOT NULL UNIQUE,
            nombre_cliente TEXT NOT NULL,
            apellido_cliente TEXT NOT NULL,
            direccion TEXT NOT NULL,
            telefono INTEGER NOT NULL,
            email_cliente TEXT NOT NULL,
            id_type INTEGER NOT NULL,
            FOREIGN KEY (id_type) REFERENCES tipo_cliente(id_type)
        )
    ''')

    #Ingresar datos iniciales 
    cur.execute("SELECT COUNT(*) FROM tipo_cliente")
    count = cur.fetchone()[0]
    if count == 0:
        tipo_clientes = [
            (101, 'plata'),
            (102, 'oro'),
            (103, 'platino'),
        ]
        cur.executemany("INSERT INTO tipo_cliente (id_type, tipo_cliente) VALUES (?, ?)", tipo_clientes)

#Confirmar cambios y manejar excepciones
    con.commit()

except:
    print("Error SQLite:", sqlite3.Error)
    if con:
        con.rollback()        


clientes = {}
usuarios = {}
idcliente = 0
idusuario = 0



def menuprincipal():
    print("================================")
    print("   M E N Ú  P R I N C I P A L   ")
    print("================================")
    print("       1.- (C) INGRESAR         ")
    print("       2.- (R) MOSTRAR          ")
    print("       3.- (U) MODIFICAR        ")
    print("       4.- (D) ELIMINAR         ")
    print("       5.- (E) Salir            ")
    print("================================")

def menumostrar():
    print("================================")
    print("     M E N Ú  M O S T R A R     ")
    print("================================")
    print("       1.- MOSTRAR TODO         ")
    print("       2.- MOSTRAR UNO          ")
    print("       3.- MOSTRAR PARCIAL      ")
    print("       4.- VOLVER               ")
    print("================================")

def ingresardatos():
    print("=================================")
    print("     INGRESAR DATOS CLIENTE      ")
    print("=================================")
    run = input("INGRESE RUN : ")
    nombre=input("INGRESE NOMBRE : ")
    apellido=input("INGRESE APELLIDO : ")
    direccion=input("INGRESE DIRECCION : ")
    fono=input("INGRESE TELEFONO : ")
    correo=input("INGRESE CORREO : ")
    tipos = [
        [101,"Plata"],[102,"Oro"],[103,"Platino"]
    ]
    print("--------------------------------------------")
    for tipo in tipos:
        print(
            " CODIGO : {} - {}.".format(tipo[0], tipo[1]))
    print("--------------------------------------------")
    tipo = input("Ingrese el codigo del Tipo de Cliente: ")
    monto=input("INGRESE MONTO CREDITO : ")
    global idcliente    
    idcliente += 1
    codigo = idcliente
    deuda = 0
    cliente = [codigo,run,nombre,apellido,direccion,fono,correo,tipo,monto,deuda]
    clientes[idcliente]=cliente

def mostrar():
    while(True):
        menumostrar()
        op2 = int(input("  INGRESE OPCIÓN : "))
        if op2 == 1:
            mostrartodo()
            input("\n\n PRESIONE ENTER PARA CONTINUAR")
        elif op2 == 2:
            mostraruno()
        elif op2 == 3:
            mostrarparcial()
        if op2 == 4:
            break
        else:
            print("Opción Fuera de Rango")

def mostrartodo():
    print("=================================")
    print("  MUESTRA DE TODOS LOS CLIENTES  ")
    print("=================================")
    for cliente,dato in clientes.items():
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                cliente, dato[1], dato[2], dato[3], dato[4], dato[5], dato[6] , dato[8], dato[9], dato[7]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")

def mostraruno():
    print("=================================")
    print("   MUESTRA DE DATOS PARTICULAR   ")
    print("=================================")
    op=int(input("\n Ingrese valor del ID del Cliente que desea Mostrar los Datos : "))
    datos = clientes.get(op)
    print(datos)
    print("\n=======================================")
    print("    MUESTRA  DE  DATOS  DEL   CLIENTE   ")
    print("=======================================")
    print(" ID            : {} ".format(datos[0]))
    print(" RUN           : {} ".format(datos[1]))
    print(" NOMBRE        : {} ".format(datos[2]))
    print(" APELLIDO      : {} ".format(datos[3]))
    print(" DIRECCION     : {} ".format(datos[4]))
    print(" FONO          : {} ".format(datos[5]))
    print(" CORREO        : {} ".format(datos[6]))
    print(" TIPO          : {} ".format(datos[9]))
    print(" MONTO CREDITO : {} ".format(datos[7]))
    print(" DEUDA         : {} ".format(datos[8]))
    print("-----------------------------------------")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")

def mostrarparcial():
    print("=======================================")
    print("   MUESTRA PARCIALMENTE LOS CLIENTES   ")
    print("=======================================")
    cant = int(input("\nIngrese la Cantidad de Clientes a Mostrar : "))
    
    datos = list(clientes.items())[:cant]
    for cliente,dato in datos:
        print(
            " ID : {} - RUN : {} - NOMBRE : {} - APELLIDO : {} - DIRECCION : {} - FONO : {} - CORREO : {} - MONTO CRÉDITO : {} - DEUDA : {} - TIPO : {} ".format(
                cliente, dato[1], dato[2], dato[3], dato[4], dato[5], dato[6] , dato[9], dato[7], dato[8]))
        print("-------------------------------------------------------------------------------------------------------------------------------------------------")
    input("\n\n PRESIONE ENTER PARA CONTINUAR")

def modificardatos():
    listanuevos=[]
    print("===================================")
    print("      MODULO MODIFICAR CLIENTE     ")
    print("===================================")
    mostrartodo()
    mod = int(input("\n Ingrese valor de ID del Cliente que desea Modificar : "))
    datos = clientes.get(mod)
    
    print(" ID         : {} ".format(datos[0]))
    listanuevos.append(datos[0])
    print(" RUN        : {} ".format(datos[1]))
    listanuevos.append(datos[1])

    opm=input("DESEA MODIFICAR EL NOMBRE : {} - [SI/NO] ".format(datos[2]))
    if opm.lower() == "si":
        nombrenuevo=input("INGRESE NOMBRE : ")
        listanuevos.append(nombrenuevo)
    else:
        listanuevos.append(datos[2])
    opm = input("DESEA MODIFICAR EL APELLIDO : {} - [SI/NO] ".format(datos[3]))
    if opm.lower() == "si":
        apellidonuevo= input("INGRESE APELLIDO : ")
        listanuevos.append(apellidonuevo)
    else:
        listanuevos.append(datos[3])
    opm = input("DESEA MODIFICAR LA DIRECCION : {} - [SI/NO] ".format(datos[4]))
    if opm.lower() == "si":
        direcnueva = input("INGRESE DIRECCION : ")
        listanuevos.append(direcnueva)
    else:
        listanuevos.append(datos[4])
    opm = input("DESEA MODIFICAR EL TELEFONO : {} - [SI/NO] ".format(datos[5]))
    if opm.lower() == "si":
        fononuevo= input("INGRESE TELEFONO : ")
        listanuevos.append(fononuevo)
    else:
        listanuevos.append(datos[5])
    opm = input("DESEA MODIFICAR EL CORREO : {} - [SI/NO] ".format(datos[6]))
    if opm.lower() == "si":
        correonuevo = input("INGRESE EL CORREO : ")
        listanuevos.append(correonuevo)
    else:
        listanuevos.append(datos[6])
    opm = input("DESEA MODIFICAR LA DEUDA : {} - [SI/NO] ".format(datos[9]))
    if opm.lower() == "si":
        deudanuevo= input("INGRESE DEUDA : ")
        listanuevos.append(deudanuevo)
    else:
        listanuevos.append(datos[9])
    opm = input("DESEA MODIFICAR EL MONTO DE CREDITO : {} - [SI/NO] ".format(datos[8]))
    if opm.lower() == "si":
        montonuevo= input("INGRESE MONTO DE CREDITO : ")
        listanuevos.append(montonuevo)
    else:
        listanuevos.append(datos[8])
    opm = input("DESEA MODIFICAR EL TIPO : {} - [SI/NO] ".format(datos[7]))
    if opm.lower() == "si":
        tipos = [
            [101,"Plata"],[102,"Oro"],[103,"Platino"]
        ]
        print("--------------------------------------------")
        for tipo in tipos:
            print(
                " CODIGO : {} - {}.".format(tipo[0], tipo[1]))
        print("--------------------------------------------")
        
        tiponuevo = input("INGRESE EL TIPO : ")
        listanuevos.append(tiponuevo)
    else:
        listanuevos.append(datos[7])
    
    clientes[mod]=listanuevos


def eliminardatos():
    print("===================================")
    print("      MODULO ELIMINAR CLIENTE      ")
    print("===================================")
    mostrartodo()
    elim = int(input("Ingrese valor de ID del Cliente que desea Eliminar : "))
    del clientes[elim]

# --------------------------------------

def menuUsuarios():
    print("================================")
    print("   M E N Ú  U S U A R I O S     ")
    print("================================")
    print("       1.-  INICIAR SESIÓN      ")
    print("       2.-  REGISTRAR USUARIO   ")
    print("       3.-  Salir               ")
    print("================================")

def contraseniaSegura():
    while True:
        contrasenia = getpass.getpass('Ingrese contraseña (debe tener letras, símbolos y al menos un número): ')

        nums = 0
        for i in range(10):
            num = str(i)
            nums += contrasenia.count(num)

        if len(contrasenia) >= 8 and not contrasenia.isalnum() and nums>=1:
            confirm_pass = input('Confirme su contraseña: ')
            if contrasenia == confirm_pass:
                print('Contraseña aceptada')
                return
            else: print('Las contraseñas no coinciden')
        else: print('No se complen todas las condiciones')
    


def ingresoUsuarios():
    print("=======================================")
    print("        INGRESO DE USUARIO             ")
    print("=======================================")

    username = input( "INGRESE NOMBRE DE USUARIO:  ")
    cur.execute('SELECT * FROM users WHERE username = ?', (username,))
    existing_user = cur.fetchone()
    if existing_user:
            print("El usuario ya existe.")
            return
    else:
        clave = contraseniaSegura()
    


    nombre = input(   "INGRESE NOMBRE           : ")
    apellidos = input("INGRESE APELLIDOS        : ")
    correo = input(   "INGRESE CORREO           : ")
    print("=======================================")
    global idusuario
    idusuario += 1
    codigo = idusuario
    usuario = [codigo,username,clave,nombre,apellidos,correo]
    usuarios[username] = usuario

#Evaluar el tipo de dato de entrada
def inputInt():
    while True:
        try:
            opUsu = int(input("INGRESE OPCIÓN: "))
            return opUsu
        except:
            print('Debe ingresar un número')

while True:
    menuUsuarios()

    opUsu = inputInt()

    if opUsu == 1:
        user = input("Ingrese nombre de usuario: ")
        clave = input("Ingrese password: ")
        if usuarios.get(user):
            usuario = usuarios.get(user)
            if usuario[2] == clave:
                print(f"Bienvenido {usuario[3]} {usuario[4]} - {usuario[2]} - id: {usuario[0]}.")
                input("Presiona ENTRAR para ingresar al Menú Principal.")
                while True:  # Bucle para el Menú Principal
                    menuprincipal()
                    op = inputInt()
                    if op == 1:
                        ingresardatos()
                    elif op == 2:
                        mostrar()
                    elif op == 3:
                        modificardatos()
                    elif op == 4:
                        eliminardatos()
                    elif op == 5:
                        opSalir = input("¿DESEA SALIR [SI/NO]: ")
                        if opSalir.lower() == "si":
                            break  # Salir del bucle del Menú Principal
                    else:
                        print("Opción Fuera de Rango")
                break  # Salir del bucle del Menú de Usuarios
            else:
                input("Contraseña incorrecta. Presiona ENTER para volver al Menú de Usuarios.")
        else:
            input("Usuario no registrado. Presiona ENTER para volver al Menú de Usuarios.")
    elif opUsu == 2:
        ingresoUsuarios()
    elif opUsu == 3:
        opSalir = input("¿DESEA SALIR [SI/NO]: ")
        if opSalir.lower() == "si":
            break
    else:
        print("Opción Fuera de Rango")