import os
import tkinter as tk
from PIL import ImageTk, Image

# Ruta de la carpeta con las imágenes
carpeta_imagenes = "IMG"

# Obtener la lista de archivos en la carpeta
archivos = os.listdir(carpeta_imagenes)

# Filtrar solo los archivos con extensión de imagen
imagenes = [archivo for archivo in archivos if archivo.endswith((".jpg", ".jpeg", ".png", ".gif"))]

# Crear una lista para almacenar los objetos ImageTk
imagenes_tk = []

def copiar_imagen_al_portapapeles(index):
    ruta_imagen = os.path.join(carpeta_imagenes, imagenes[index])

    # Crear una instancia de la imagen
    imagen_pil = Image.open(ruta_imagen)

    # Copiar la imagen al portapapeles
    imagen_pil.copy().show()
    print(f"La imagen {imagenes[index]} se ha copiado al portapapeles.")


def mostrar_imagen(index):
    imagen_actual = imagenes_tk[index]
    canvas.configure(image=imagen_actual)
    canvas.image = imagen_actual

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Galería de Imágenes")

# Crear un scrollbar
scrollbar = tk.Scrollbar(ventana)
scrollbar.pack(side="right", fill="y")

# Crear un lienzo para mostrar las imágenes
canvas = tk.Canvas(ventana, yscrollcommand=scrollbar.set)
canvas.pack(side="left", fill="both", expand=True)

# Configurar el scrollbar
scrollbar.config(command=canvas.yview)

# Crear un frame para las imágenes
marco_imagenes = tk.Frame(canvas)
marco_imagenes.pack()

# Configurar el espaciado y el número de columnas
espaciado = 9
columnas = 5

# Cargar las imágenes y mostrarlas en el frame
for i, imagen in enumerate(imagenes):
    ruta_imagen = os.path.join(carpeta_imagenes, imagen)
    imagen_pil = Image.open(ruta_imagen)

    # Redimensionar la imagen a 1/3 de su tamaño original
    nuevo_ancho = int(imagen_pil.width / 3)
    nuevo_alto = int(imagen_pil.height / 3)
    imagen_pil = imagen_pil.resize((nuevo_ancho, nuevo_alto))

    imagen_tk = ImageTk.PhotoImage(imagen_pil)
    imagenes_tk.append(imagen_tk)

    fila = i // columnas
    columna = i % columnas

    etiqueta_imagen = tk.Label(marco_imagenes, image=imagen_tk)
    etiqueta_imagen.grid(row=fila, column=columna, padx=espaciado, pady=espaciado)

    etiqueta_imagen.bind("<Double-Button-1>", lambda event, index=i: copiar_imagen_al_portapapeles(index))

# Actualizar el tamaño del lienzo y habilitar el desplazamiento
marco_imagenes.update_idletasks()
canvas.config(scrollregion=canvas.bbox("all"))

# Ejecutar el bucle principal de la aplicación
ventana.mainloop()
