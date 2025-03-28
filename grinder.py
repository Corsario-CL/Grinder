import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk  # Importar para el combo box
from PIL import Image, ImageTk
import os

# Función para convertir la imagen
def convert_image():
    try:
        # Abrir el diálogo para seleccionar cualquier tipo de archivo
        input_path = filedialog.askopenfilename(title="Selecciona un archivo", filetypes=[("Todos los archivos", "*.*")])
        if not input_path:  # Si no se selecciona un archivo, termina la función
            return

        # Verificar si el archivo es una imagen válida
        try:
            img = Image.open(input_path)
        except IOError:
            messagebox.showerror("Error", "El archivo seleccionado no es una imagen válida.")
            return

        # Obtener el formato de salida seleccionado por el usuario
        output_format = format_combobox.get()

        if not output_format:  # Si no se selecciona un formato, muestra un error
            messagebox.showerror("Error", "Por favor, selecciona un formato de salida.")
            return

        # Abrir el diálogo para seleccionar la ruta de guardado
        output_path = filedialog.asksaveasfilename(defaultextension=f".{output_format.lower()}", filetypes=[("Archivos de imagen", f"*.{output_format.lower()}")])
        if not output_path:  # Si no se selecciona una ruta de guardado, termina la función
            return

        # Guardar la imagen en el formato seleccionado
        img.save(output_path, format=output_format.upper())

        # Mostrar la imagen convertida en la ventana
        show_converted_image(output_path)

        # Informar al usuario sobre el éxito de la conversión
        messagebox.showinfo("Éxito", f"Imagen convertida y guardada como: {output_path}")

    except Exception as e:
        messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

# Función para mostrar la imagen convertida en la interfaz
def show_converted_image(image_path):
    try:
        # Abrir la imagen convertida
        img = Image.open(image_path)

        # Convertir la imagen a un formato que pueda mostrar Tkinter
        img.thumbnail((250, 250))  # Redimensionar la imagen para que se ajuste
        img_tk = ImageTk.PhotoImage(img)

        # Si ya hay una imagen mostrada, la reemplazamos
        if hasattr(show_converted_image, "image_label"):
            show_converted_image.image_label.config(image=img_tk)
            show_converted_image.image_label.image = img_tk
        else:
            # Crear un label para mostrar la imagen
            show_converted_image.image_label = tk.Label(root, image=img_tk, bg="#2e2e2e")
            show_converted_image.image_label.image = img_tk  # Guardamos la referencia
            show_converted_image.image_label.pack(pady=20)
        
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo mostrar la imagen convertida: {str(e)}")

# Crear la ventana principal
root = tk.Tk()
root.title("Grinder - Convertidor de Imágenes")
root.geometry("600x700")
root.resizable(False, False)

# Fondo con color degradado (más atractivo)
root.configure(bg='#2e2e2e')

# Título
title_label = tk.Label(root, text="Grinder", font=("Helvetica", 28, "bold"), fg="white", bg="#2e2e2e")
title_label.pack(pady=20)

# Descripción
desc_label = tk.Label(root, text="Convierte imágenes entre diferentes formatos.", font=("Helvetica", 14), fg="white", bg="#2e2e2e")
desc_label.pack(pady=10)

# Frame para agrupar la selección del formato y la imagen
frame = tk.Frame(root, bg="#2e2e2e")
frame.pack(pady=10)

# Crear un combobox para seleccionar el formato
format_label = tk.Label(frame, text="Selecciona el formato de salida", font=("Helvetica", 12), fg="white", bg="#2e2e2e")
format_label.pack(pady=5)

format_combobox = ttk.Combobox(frame, values=[
    "JPG", "PNG", "WEBP", "BMP", "GIF", "TIFF", "EPS", "PDF", "ICO", "HEIF", "AVIF", "PCX", "PBM"
], state="readonly", width=10)
format_combobox.set("JPG")  # Formato por defecto
format_combobox.pack(pady=5)

# Botón de conversión
convert_button = tk.Button(root, text="Convertir Imagen", font=("Helvetica", 14), fg="white", bg="#4CAF50", activebackground="#45a049", relief="flat", command=convert_image)
convert_button.pack(pady=20)

# Mostrar imagen convertida (si se convierte una imagen)
show_converted_image_label = tk.Label(root, text="Imagen convertida aparecerá aquí.", font=("Helvetica", 12), fg="white", bg="#2e2e2e")
show_converted_image_label.pack(pady=10)

# Footer (Derechos de autor)
footer_label = tk.Label(root, text="© 2025 Grinder - Todos los derechos reservados", font=("Helvetica", 8), fg="gray", bg="#2e2e2e")
footer_label.pack(side="bottom", pady=10)

# Ejecutar la ventana
root.mainloop()
