
# 🔐 Proyecto Cripto-Estego en Python

Este proyecto es una herramienta educativa desarrollada en Python para experimentar con **criptografía** y **esteganografía**, utilizando una interfaz gráfica construida con **Tkinter**. Su objetivo es demostrar el uso de algoritmos, estructuras de datos y procesamiento de imágenes sin recurrir a librerías criptográficas externas.

## Integrates

- De Souza Franco, Legajo: 1179618
- Hassan Ayelen, Legajo: 121072
- Squeo Paloma, Legajo: 1208949
- Troitiño Valentin, Legajo:  1205019


## Características

- Cifrado y descifrado de mensajes usando distintos algoritmos:
  - César
  - Vigenère
  - Hill Cipher
  - XOR mejorado
  - Transposición
  - AES
  - Bifid
- Cifrado y descifrado de archivos.
- Generación de claves aleatorias (basadas en imagen o independientes).
- Ocultamiento y recuperación de mensajes en imágenes mediante esteganografía (LSB).
- Interfaz gráfica simple e intuitiva desarrollada con Tkinter.

## Fases

### Fase 1 - 40%
- Implementación inicial de cifrados básicos (César, Vigenère).
- Implementación del cifrado de archivos.
- Creación de una interfaz gráfica simple.
- Soporte para ingreso y visualización de mensajes cifrados.
### Fase 2 - 80%
- Inclusión de cifrados más avanzados (Hill, XOR, Feistel).
- Implementación de esteganografía en imágenes (LSB).
- Implementación de otros métodos de esteganografía
- Generación de claves aleatorias y basadas en imágenes.
### Fase 3 - 100%
- Implementación del Cifrado AES
- Documentación completa del código y uso del programa.
- Búsqueda de errores y optimización.

## Instalación

### 1. Clonar el repositorio
```bash
git clone https://github.com/vtroitino-uade/Proyecto-Cripto-Estego.git
cd Proyecto-Cripto-Estego
```
### 2. Crear un entorno virtual
```bash
  python -m venv env
```
### 3. Activar entorno virtual
```bash
  .\env\Scripts\activate
```
### 4. Instalar dependencias
```bash
  pip install -r requirements.txt
```
## ❗Aclaración❗

Este proyecto fue desarrollado como parte del curso Algoritmos y Estructuras de Datos I con fines educativos. No está diseñado para aplicaciones de seguridad real.

