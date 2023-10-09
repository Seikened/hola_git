import os

directorio = os.getcwd()
print("El directorio actual es: ", directorio)
listadoArchivos = os.listdir(directorio)
archivo = "test.py"
destino = os.path.join(directorio, "test_copia.py")
if archivo in listadoArchivos:
	os.system(f"cp {archivo} {destino}")


# moverme atras en mac en terminal