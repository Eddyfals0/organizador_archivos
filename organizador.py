import os


#obtiene el directorio en el que estamos con getcwd()
directorio_base = os.getcwd()
print(f"directorio actual: {directorio_base}")

carpetas_a_crear = ["imagenes", "documentos", "videos"]

for carpeta in carpetas_a_crear:
    #Construye la direccion desde el drirectorio base y conectandolo a la carrpeta que queremos crear
    ruta_completa =os.path.join(directorio_base, carpeta)
    print(ruta_completa)
    
    #verifica si no exista ya al carpeta
    if not os.path.exists(ruta_completa):
        os.mkdir(ruta_completa)
        print(f"Carpeta: {ruta_completa} añadida")
    else:
        print(f"Carpeta {ruta_completa} ya creada")

print("\nContenido del directorio:")

#muestra en una lista los elementos del directorio
contenido= os.listdir(directorio_base)
for elementos in contenido:
    print(f"- {elementos}")

nombre_antiguo = "prueba_temporal.txt"
nombre_nuevo = "archivo_renombrado.txt"

#creamos un achov con with open con le nombre temporal
with open(nombre_antiguo, "w") as f:
    f.write("Este es un archivo de prueba :3")
    
print(f"\nArchivo: {nombre_antiguo}, creado")

#mueve o renombra archivos 
os.rename(nombre_antiguo, nombre_nuevo)

print(f"Archivo renombrado como: {nombre_nuevo}.")
print("hola")
    
archivo_a_eliminar = nombre_nuevo

