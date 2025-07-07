# 🔐 Proyecto Cripto-Estego

Este proyecto es una herramienta educativa desarrollada en Python para experimentar con **criptografía** y **esteganografía**, utilizando una interfaz gráfica construida con **CustomTkinter**. Su objetivo es demostrar el uso de algoritmos, estructuras de datos y procesamiento de imágenes sin recurrir a librerías criptográficas externas.

## Integrates

- De Souza Franco, Legajo: 1179618
- Hassan Ayelen, Legajo: 1210723
- Squeo Paloma, Legajo: 1208949
- Troitiño Valentin, Legajo:  1205019

## 📁 Índice

1. [Características](#características)
2. [Fases](#fases)
3. [Instalación](#instalación)
4. [Encriptación](#encriptación)
    * [Cifrado César](#cifrado-césar)
    * [Cifrado Vigenère](#cifrado-vigenère)
    * [Cifrado XOR](#cifrado-xor)
    * [Cifrado Feistel](#cifrado-feistel)
    * [Cifrado Hill](#cifrado-hill)
5. [Esteganografía](#esteganografía)
6. [Generación de Claves](#generación-de-claves)

## Características

- Cifrado y descifrado de mensajes usando distintos algoritmos:
  - César
  - Vigenère
  - XOR
  - Feistel
  - Hill
- Generación de claves aleatorias
- Ocultamiento y recuperación de mensajes en imágenes mediante esteganografía (LSB).
- Interfaz gráfica simple e intuitiva desarrollada con CustomTkinter.

## Fases

#### Fase 1 - 40%
- Implementación inicial de cifrados básicos (César, Vigenère).
- Implementación del cifrado de archivos.
- Creación de una interfaz gráfica simple.
#### Fase 2 - 80%
- Inclusión de cifrados más avanzados (Hill, XOR, Feistel).
- Implementación de esteganografía en imágenes (LSB).
- Generación de claves aleatorias.
#### Fase 3 - 100%
- Documentación completa del código y uso del programa.
- Implementación de logs.

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

## 🔐 Encriptación

Desde la pestaña **Encriptación**, podés seleccionar el tipo de cifrado deseado, ingresar un mensaje y una clave (o generar una aleatoria), y cifrar el contenido.

Las principales opciones son:

* **Escribir mensaje manualmente**: se puede ingresar el mensaje directamente en el campo correspondiente.

* **Seleccionar tipo de cifrado**: se puede elegir entre los métodos de cifrado disponibles (César, Vigenère, XOR, Feistel, Hill). Cada uno tiene sus requisitos y características específicas.

* **Ingresar clave**: escribí una clave personalizada o usá el botón de generación automática. El formato de la clave varía según el tipo de cifrado. Siempre usar la misma clave para descifrar un mensaje.

* **Seleccionar un alfabeto**: aplicable solo a cifrados César y Vigenère. Podés usar un alfabeto predefinido (Español, Inglés, ASCII) o ingresar uno personalizado.

* **Cifrar o descifrar**: ejecutar la acción elegida con los parámetros seleccionados.

* **Cargar archivo (.txt)**: permite importar texto desde un archivo para usarlo como mensaje original. Útil si querés cifrar textos largos o existentes.

Algunos cifrados producen resultados que incluyen caracteres no imprimibles, como los de control [ASCII](https://elcodigoascii.com.ar/) (por ejemplo, tabulaciones, saltos de línea, etc.). Para evitar problemas al mostrar o guardar estos resultados, el programa los convierte automáticamente a formato [Base64](https://kapilyadav22.medium.com/base-64-encoding-502e522bb3ad), una forma segura y legible de representar datos binarios como texto.

#### Cifrado César

El cifrado César es un cifrado por sustitución en el que cada letra del mensaje se reemplaza por otra que se encuentra un número fijo de posiciones más adelante en el alfabeto.
```
* Mensaje: Texto alfanumérico
* Clave: Número entero (desplazamiento)
* Alfabeto: Se puede seleccionar entre Español, Inglés, ASCII o un alfabeto personalizado.

Ejemplo: Mensaje = `HOLA`, Clave = 3, Alfabeto = `Inglés` → Resultado: `KROD`
```

#### Cifrado Vigenère

Es un cifrado polialfabético que utiliza una palabra clave para aplicar desplazamientos diferentes a cada letra del mensaje utilizado un alfabeto.
```
* Mensaje: Texto alfanumérico
* Clave: Palabra o secuencia de letras (sin espacios)
* Alfabeto: Se puede seleccionar entre Español, Inglés, ASCII o un alfabeto personalizado.

Ejemplo: Mensaje = `HOLA`, Clave = `CLAVE`, Alfabeto = `Inglés` → Resultado: `OIWUDNI`
```

#### Cifrado XOR

Este cifrado opera a nivel binario, aplicando la operación XOR entre el mensaje y la clave.
```
* Mensaje: Texto alfanumérico
* Clave: Texto alfanumérico

Ejemplo: Mensaje = `HOLA`, Clave = `CLAVE` → Resultado: `CwMNFw==` (Base64)
```

#### Cifrado Feistel

Basado en la estructura Feistel, este cifrado divide el mensaje en dos mitades y aplica varias rondas de funciones sobre ellas usando subclaves generadas desde una clave principal.
```
* Mensaje: Texto alfanumérico
* Clave `<clave>:<rondas>`:
    <clave>: Texto alfanumérico
    <rondas>: Número entero mayor a 0
    Ejemplo de Clave: `mi_clave:4`

Ejemplo: Mensaje = `HOLA`, Clave = `mi_clave:4` → Resultado: `fX5LemxhdmVYWFhYWFhYWA==:12` (Base64)
```
#### Cifrado Hill

Cifrado basado en álgebra lineal que utiliza multiplicación de vectores de letras por matrices. La matriz debe ser invertible módulo 26 para permitir el descifrado.
```
* Mensaje: Texto alfanumérico
* Clave: Matriz cuadrada 2x2 o 3x3, ingresada como números separados por espacio.
    |-> Ejemplos válidos:
        * 2x2: `12 13 1 9`
        * 3x3: `6 24 1 13 16 10 20 17 15`

Ejemplo: Mensaje = `HOLA`, Clave = `12 13 1 9` → Resultado: `004GDCL`
```
## 🖼 Esteganografía
Desde la pestaña Esteganografía se pueden ocultar y extraer mensajes dentro de imágenes utilizando la técnica **LSB Matching** (Least Significant Bit Matching), una forma de modificar los bits menos significativos de los píxeles sin alterar perceptiblemente la imagen. Desde la interfaz gráfica podés realizar las siguientes acciones:

* **Ocultar mensaje:**

  1. Seleccionar imagen (`.jpg`, `.jpeg`, `.png`, `.bmp` o `.ppm`).
  2. Escribir el mensaje.
  3. Hacer click en **Ocultar** para generar una nueva imagen con el mensaje oculto.

o

* **Extraer mensaje:**

  1. Seleccionar imagen con mensaje oculto.
  2. Hacer clic en **Extraer** para ver el mensaje embebido.

## 🔑 Generación de Claves

En cada tipo de cifrado hay un botón **Generar** que produce una clave aleatoria válida para el algoritmo seleccionado.

* **César:** Número aleatorio entre 1 y tamaño de alfabeto.
* **Vigenère / XOR / Feistel:** Palabra aleatoria
* **Feistel:** Formato `clave:rondas`, con clave y rondas aleatorias
* **Hill:** Genera una matriz 2x2 o 3x3 aleatoria e invertible módulo 26
