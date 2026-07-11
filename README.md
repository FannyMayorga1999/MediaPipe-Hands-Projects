# Control por Gestos — Plantas, Puzzles, Luces y Matrix

Aplicaciones interactivas que utilizan la cámara web y **MediaPipe Hands** para detectar gestos de la mano en tiempo real. Incluye una planta virtual que crece con los dedos, tres versiones de un puzzle de 3×3 controlado por gestos, un panel de luces virtuales, y dos interfaces estilo The Matrix para control y hackeo.

---

## Programas incluidos

### 1. Planta Interactiva
**Archivo:** `flores y mano.ipynb` (1er programa)
- Controla una planta virtual con las manos:
  - **Mano derecha** → altura del tallo
  - **Mano izquierda** → tamaño de las flores
- Usa distancia pulgar–índice (gesto de pinza)

### 2. Puzzle de Gestos — Versión 1 (Básica)
- Puzzle 3×3 con IDs numéricos
- Mueve la mano sobre las celdas para intercambiar piezas
- Gana cuando todas las piezas están en orden

### 3. Puzzle de Gestos — Versión 2 (Puntero)
- Toma una foto con la cámara (ESPACIO)
- Arrastra las piezas con el dedo índice
- La pieza se pega al dedo mientras lo detecte

### 4. Puzzle de Gestos — Versión 3 (Pinza)
- Similar a V2 pero usa gesto de pinza (pellizco)
- Cerrar pinza → agarrar pieza
- Abrir pinza → soltar pieza

### 5. Luz por Dedo
**Archivo:** `luz_por_dedo.ipynb`
- Cada dedo levantado enciende una luz virtual de color:
  - **Pulgar** → BLANCA
  - **Índice** → ROJA
  - **Medio** → VERDE
  - **Anular** → AZUL
  - **Meñique** → AMARILLA
- Detecta los 5 dedos individualmente usando MediaPipe Hands
- Ideal para demostrar mapeo de señales digitales (Álgebra Lineal)

### 6. Fotos según Número de Dedos
**Archivo:** `fotos_por_dedos.ipynb`
- Toma una foto automática al mostrar 0–5 dedos durante ~2 segundos
- Guarda las imágenes en `fotos_capturadas/` con timestamp

### 7. Interface Matrix — UNIBE
**Archivo:** `cyberpunk_interface.ipynb`
- Interfaz estilo The Matrix con 5 canales UNIBE
- Cada dedo levantado activa un nodo con lluvia de caracteres cayendo
- Mapeo de dedos a letras:
  - **Pulgar** → U
  - **Índice** → N
  - **Medio** → I
  - **Anular** → B
  - **Meñique** → E
- Efecto visual cyberpunk con nodos brillantes y conexiones entre dedos activos
- Barra de estado inferior muestra nodos activos

### 8. Simulador de Hackeo — Interface Matrix
**Archivo:** `puzzcle_letras.ipynb`
- Juego interactivo inspirado en The Matrix
- Captura letras objetivo usando gesto de pinza (pulgar + índice)
- Lluvia de caracteres estilo Matrix
- 3 niveles de dificultad:
  1. UNIBE
  2. UNIVERSIDAD
  3. INGENIERIA
- Cronómetro por nivel y ranking de mejores tiempos
- Pausa con mano abierta
- Botones virtuales (INICIAR, NUEVO JUEGO, SALIR) con gesto de pinza

---

## Requisitos

| Dependencia  | Versión  |
|-------------|----------|
| Python      | 3.12.10  |
| OpenCV      | 5.0.0    |
| MediaPipe   | 0.10.14  |
| NumPy       | 2.5.0    |

---

## Instalación

```bash
# Instalar dependencias
pip install opencv-python mediapipe==0.10.14 numpy
```

> **Nota:** MediaPipe 0.10.14 es la versión recomendada para compatibilidad.

---

## Uso

Abre el notebook en Jupyter:

```bash
jupyter notebook "luz_por_dedo.ipynb"
```

Ejecuta la celda del programa que quieras usar.

### Controles comunes
| Tecla     | Acción                           |
|-----------|----------------------------------|
| `ESC`     | Salir del programa               |
| `X`       | Cerrar ventana                   |
| `ESPACIO` | Tomar foto (Puzzle V2, V3)       |
| `R`       | Reiniciar (Puzzle V2, V3)        |

---

## Estructura del proyecto

```
python/
├── cyberpunk_interface.ipynb  # Interface Matrix UNIBE (nodos por dedo)
├── flores y mano.ipynb        # Planta virtual interactiva
├── fotos_por_dedos.ipynb      # Captura de fotos según cantidad de dedos
├── luz_por_dedo.ipynb         # Luces virtuales por cada dedo
├── puzzle_gestos_mano.ipynb   # Puzzle con gestos (3 versiones)
├── puzzcle_letras.ipynb       # Puzzle de letras
├── fotos_capturadas/          # Fotos tomadas por fotos_por_dedos.ipynb
├── README.md                  # Este archivo
└── .gitignore                 # Archivos ignorados
```
