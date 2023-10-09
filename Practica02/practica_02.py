# Integrantes:
# Edgar Mauricio Trejo Delgado
# Gael Arturo Muñoz Delgado
# Fernando Leon Franco

# Obtener el directorio actual


import os

def calculoTiempo(tiempo):
	# Tiempo en segundos desde la época
	tiempo_epoch = tiempo

	# Desglosar el tiempo
	minutos, segundos = divmod(tiempo_epoch, 60)
	horas, minutos = divmod(minutos, 60)
	dias, horas = divmod(horas, 24)
	anios, dias = divmod(dias, 365.25)
	anios = int(anios)
	dias = int(dias)
	horas = int(horas)
	minutos = int(minutos)
	segundos = int(segundos)

	# Ajustar para la época (1970)
	anios += 1970

	return anios,dias,horas,minutos,segundos


carpetaC1 = "c1"
carpetaC2 = "c2"

# Crear un directorio llamado c1 y su verificación
nombreDirectorio = "c1"
os.makedirs(nombreDirectorio, exist_ok=True)
rutaC1 = os.path.join(os.getcwd(),nombreDirectorio)

if os.path.exists(nombreDirectorio):
	print(f"Se creo correcramente {nombreDirectorio}")

else:
	print(f"No se creo correcramente {nombreDirectorio} intentalo nuevamente")


# Crear un directorio llamado c2 y su verificación
nombreDirectorio = "c2"
os.makedirs(nombreDirectorio, exist_ok=True)
rutaC2 = os.path.join(os.getcwd(),nombreDirectorio)

if os.path.exists(nombreDirectorio):
	print(f"Se creo correcramente {nombreDirectorio}")
else:
	print(f"No se creo correcramente {nombreDirectorio} intentalo nuevamente")


# Crear un archivo de texto archivo_c1.txt y en el excribe "Este es un archivo de texto de c1"
	# Y este debe estar guardado en el "c1"
nombreArchivo = "archivo_c1.txt"
rutaArchivoC1 = os.path.join(rutaC1,nombreArchivo)
# Documents/Practica02/c1/archivo_c1.txt

if os.path.exists(rutaArchivoC1):
	print(f"El archivo: {nombreArchivo} ya ha sido creado")
else:
	print(f"El archivo se creo correctamente {nombreArchivo} ")
	with open(rutaArchivoC1, "w") as f:
		f.write("ESTE ES UN ARCHIVO DE TEXTO DE C1")


# Crear un archivo de texto archivo_c2.txt y en el excribe "Este es un archivo de texto de c2"
	# Y este debe estar guardado en el "c2"
nombreArchivo = "archivo_c2.txt"
rutaArchivoC2 = os.path.join(rutaC2,nombreArchivo)
# Documents/Practica02/c2/archivo_c2.txt

if os.path.exists(rutaArchivoC2):
	print(f"El archivo: {nombreArchivo} ya ha sido creado")
else:
	print(f"El archivo se creo correctamente {nombreArchivo} ")
	with open(rutaArchivoC2, "w") as f:
		f.write("ESTE ES UN ARCHIVO DE TEXTO DE C2")


# Obtener el directorio actual
directorio = os.getcwd()
print("El directorio actual es: ", directorio)

# Listar todos los archivos de un directorio
listaArchivos = os.listdir(directorio)
print("Los archivos del directorio son: ", listaArchivos)

# Crear un directorio llamado modulos y su verificación
nombreDirectorio = "modules"
os.makedirs(nombreDirectorio, exist_ok=True)

# Crear un directorio llamado modulos y su verificación
if os.path.exists(nombreDirectorio):
	print(f"Se creo correcramente {nombreDirectorio}")

else:
	print(f"No se creo correcramente {nombreDirectorio} intentalo nuevamente")

# Manejo de archivos

# Crear un archivo de texto README.txt y en el excribe "Este es un archivo README"
	# Y este debe estar guardado en el "modules"

# Nos movemos de ruta
rutaModules = os.path.join(directorio, nombreDirectorio)
os.chdir(rutaModules)

# Creación de archivo
nombreArchivo = "README.txt"
rutaReadme = os.path.join(os.getcwd(),nombreArchivo)
# Documents/Practica02/modules/README.txt

if os.path.exists(rutaReadme):
	print(f"El archivo: {nombreArchivo} ya ha sido creado")


else:
	print(f"El archivo se creo correctamente {nombreArchivo} ")
	with open(nombreArchivo, "w") as f:
		f.write("ESTE ES UN ARCHIVO README")





# Muestra la información detallada sobre el archivo
mostarInfor = os.stat(rutaReadme)
fechaModificacion = calculoTiempo(mostarInfor.st_mtime)

print(f"""
Tamaño del archivo: {mostarInfor.st_size} bytes
Fecha de modificación: {fechaModificacion}
""")

# Ruta origen y destino de C1
os.chdir('..')
directorio = os.getcwd()
print("El directorio actual es: ", directorio)
rutaC1Origen = os.path.join(directorio, os.path.join(carpetaC1,"archivo_c1.txt"))
print("El directorio actual es: ", rutaC1Origen)
rutaC1Destino = os.path.join(rutaModules,"archivo_c1.txt")
print("El directorio actual es: ", rutaC1Destino)

# Ruta origen y destino de C2
rutaC2Origen = os.path.join(directorio, os.path.join(carpetaC2,"archivo_c2.txt"))
print("El directorio actual es: ", rutaC2Origen)
rutaC2Destino = os.path.join(rutaModules,"archivo_c2.txt")
print("El directorio actual es: ", rutaC2Destino)


# Mover los archivos de C1

with open(rutaC1Origen, 'rb') as f_origen:
    with open(rutaC1Destino, 'wb') as f_destino:
        f_destino.write(f_origen.read())

# Mover los archivos de C2

with open(rutaC2Origen, 'rb') as f_origen:
	with open(rutaC2Destino, 'wb') as f_destino:
		f_destino.write(f_origen.read())

# Renombrar c1 y c2
nuevoC1 = "archivo_c1_copia.txt"
nuevoC2 = "archivo_c2_copia.txt"
if os.path.exists(rutaC1Destino):
	os.rename(rutaC1Destino, os.path.join(rutaModules, nuevoC1))
else:
	print("No se pudo renombrar el archivo")

if os.path.exists(rutaC2Destino):
	os.rename(rutaC2Destino, os.path.join(rutaModules, nuevoC2))
else:
	print("No se pudo renombrar el archivo")


listaDeC1 = os.listdir(os.path.join(directorio, carpetaC1))
print("Los archivos del directorio son: ", listaDeC1)
listaDeC2 = os.listdir(os.path.join(directorio, carpetaC2))
print("Los archivos del directorio son: ", listaDeC2)

# Listar todos los archivos de un directorio de C1
for archivo in listaDeC1:
	print("El archivo a eliminar es: ", archivo)
	os.remove(os.path.join(directorio, os.path.join(carpetaC1,archivo)))

# Listar todos los archivos de un directorio de C2
for archivo in listaDeC2:
	print("El archivo a eliminar es: ", archivo)
	os.remove(os.path.join(directorio, os.path.join(carpetaC2,archivo)))