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

contenido= os.listdir(directorio_base)
for elementos in contenido:
    print(f"- {elementos}")

