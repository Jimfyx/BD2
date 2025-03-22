from modelos.cllinicaUpana import clinica

def crearcionEspecialidad():
    nuevaEspecialidad = input("Diga la Especialidad: ")
    miclinica = clinica()
    msg, id = miclinica.insertarCatalogoEsecialidades(nuevaEspecialidad)
    print(msg)

def verEspecialidades():
    miclinica = clinica()
    msg,reg = miclinica.obtenerEspecialista()
    reg = list(reg)
    print(msg, reg)


def crearDoctor():
    nombre = input("Diga el nombre del doctor: ")
    apellido = input("Diga el apellido del doctor: ")
    print("Escoja una especialidad")
    miclinica = clinica()

    msg, reg = miclinica.obtenerEspecialista()
    listadoEspecialistas = list(reg)
    i = 0
    for esp in listadoEspecialistas:
        i = i +1
        esp["indice"] = i

        print(f"{esp["indice"]} - {esp["especialidad"]}")
    especialidadNumerica = input("Escoja la especialidad: ")
    especialidadEscogida=""
    for esp in listadoEspecialistas:
        if str(esp["indice"]) ==  especialidadNumerica:
            especialidadEscogida = esp["_id"]
    _otrosDatos = input("Desea agregar otros datos(s/n): ")
    otroDato ={}
    if _otrosDatos == "s":
        campo = input("Que campo desea insertar: ")
        valor = input("Inserte el valor: ")
        otroDato[campo] = valor
    msg = miclinica.insertarDoctores(nombre,apellido, especialidadEscogida,otroDato)
    print(msg)


def actualizarDoctor():
    miclinica = clinica()
    msg, doctores = miclinica.obtenerDoctores()
    listadoDoctores = list(doctores)
    i = 0
    print("Elija un doctor")
    for doctor in listadoDoctores:
        i = i +1
        doctor["indice"] = i
        nombre = doctor['nombre'][0]['nombre'] if doctor['nombre'] else 'Desconocido'
        apellido = doctor['apellido'][0]['apellido'] if doctor['apellido'] else 'Desconocido'
        print(f"{doctor["indice"]} - {nombre} {apellido}")
    doctorElegido = input("")
    doctorEligidoId = ""
    for doctor in listadoDoctores:
        if str(doctor["indice"]) == doctorElegido:
            doctorEligidoId =str(doctor["_id"])
    # buscamos la especialidad
    msg, reg = miclinica.obtenerEspecialista()
    listadoEspecialistas = list(reg)
    i = 0
    for esp in listadoEspecialistas:
        i = i + 1
        esp["indice"] = i

        print(f"{esp["indice"]} - {esp["especialidad"]}")
    especialidadNumerica = input("Escoja la especialidad: ")
    especialidadEscogida = ""
    for esp in listadoEspecialistas:
        if str(esp["indice"]) == especialidadNumerica:
            especialidadEscogida = esp["_id"]

    msg, contador = miclinica.actualizarEspecialidadDoctores(doctorEligidoId,especialidadEscogida)


opcion = "n"
while opcion != 's':
    print("Hola bienvenidos al sistema de control de citas Upana")
    print("Por favor elija una opcion")
    print("1.- Crear Especialidad")
    print("2.- Ver Especialistas")
    print("3.- Insertar Doctor")
    print("4.- Actualizar Doctores")
    print("s.- Salir")
    opcion = input()

    if opcion == "1":

        crearcionEspecialidad()
    elif opcion == "2":
        verEspecialidades()
    elif opcion == "3":
        crearDoctor()
    elif opcion == "4":
        actualizarDoctor()

