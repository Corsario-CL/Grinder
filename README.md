# Grinder - Convertidor de Imágenes

**Grinder** es una herramienta de conversión de imágenes que permite transformar imágenes entre diferentes formatos. Con una interfaz gráfica moderna y fácil de usar, puedes seleccionar una imagen, elegir el formato de salida y guardar el archivo convertido en tu sistema. ¡Todo esto desde una sola ventana!

## Características

- **Soporte para múltiples formatos de imagen**: Convierte imágenes entre formatos como JPG, PNG, WEBP, BMP, GIF, TIFF, EPS, PDF, ICO, HEIF, AVIF, PCX, PBM, entre otros.
- **Interfaz gráfica fácil de usar**: Diseño intuitivo con Tkinter que permite seleccionar archivos de imagen y elegir el formato de salida.
- **Compatibilidad de sistemas**: Funciona en sistemas operativos Windows, macOS y Linux.
- **Soporte de múltiples tipos de archivo**: Puedes seleccionar cualquier archivo de imagen (y otros archivos) para su conversión.

## Instalación

Para usar **Grinder**, asegúrate de tener Python 3.x instalado en tu sistema.

### Requisitos

- Python 3.6 o superior
- Pillow (Biblioteca para manejo de imágenes)
- Tkinter (Interfaz gráfica)

### Instrucciones de instalación

1. Clona el repositorio:

    ```bash
    git clone https://github.com/tuusuario/grinder.git
    ```

2. Navega a la carpeta del proyecto:

    ```bash
    cd grinder
    ```

3. Instala las dependencias necesarias utilizando `pip`:

    - Si usas un entorno virtual (recomendado):

    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Para Linux/macOS
    venv\Scripts\activate     # Para Windows
    pip install -r requirements.txt
    ```

    - Si no usas un entorno virtual, instala las dependencias globalmente:

    ```bash
    pip3 install pillow
    ```

4. Para ejecutar el programa, simplemente corre el siguiente comando:

    ```bash
    python3 grinder.py
    ```

## Uso

1. Ejecuta el programa (`grinder.py`) con el comando mencionado anteriormente.
2. Selecciona una imagen que desees convertir utilizando el botón "Seleccionar imagen".
3. Elige el formato de salida desde el menú desplegable.
4. Selecciona la ubicación en tu computadora para guardar la imagen convertida.
5. Haz clic en el botón "Convertir Imagen" para completar la conversión.

## Capturas de Pantalla

<img src="https://github.com/user-attachments/assets/15ca8e4c-310e-4880-b912-2cbfcb7f9b89" width="500">
<img src="https://github.com/user-attachments/assets/915be4d9-9dda-4a09-9b9f-4ca89fd3d51d" width="500">

## Contribuciones

¡Las contribuciones son bienvenidas! Si tienes una idea o mejora para **Grinder**, por favor crea un **fork** del repositorio y envía un **pull request**. Asegúrate de seguir estos pasos:

1. Haz un **fork** de este repositorio.
2. Crea una rama para tu nueva característica (`git checkout -b feature/mi-nueva-caracteristica`).
3. Realiza tus cambios y haz commit (`git commit -am 'Agrega nueva característica'`).
4. Empuja tu rama al repositorio (`git push origin feature/mi-nueva-caracteristica`).
5. Abre un pull request en GitHub.

## Licencia

Este proyecto está licenciado bajo la Licencia GNU General Public License v3.0 - consulta el archivo [LICENSE](LICENSE) para más detalles.

---

> **Grinder** es una herramienta de código abierto creada para ayudar a las personas a convertir imágenes de manera rápida y sencilla. ¡Gracias por utilizarla!

---

Si necesitas agregar alguna sección más o ajustar la información, avísame y estaré encantado de ayudarte.


