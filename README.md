# Control por Gestos — Plantas, Puzzles y Luces

Aplicaciones interactivas que utilizan la cámara web y **MediaPipe Hands** para detectar gestos de la mano en tiempo real. Incluye una planta virtual que crece con los dedos, tres versiones de un puzzle de 3×3 controlado por gestos, y un panel de luces virtuales que se encienden según el dedo levantado.

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
├── flores y mano.ipynb      # Notebook principal (4 programas)
├── fotos_por_dedos.ipynb    # Captura de fotos según cantidad de dedos
├── luz_por_dedo.ipynb       # Luces virtuales por cada dedo
├── puzzle_gestos_mano.ipynb # Puzzle con gestos (3 versiones)
├── fotos_capturadas/        # Fotos tomadas por fotos_por_dedos.ipynb
├── README.md                # Este archivo
└── .gitignore               # Archivos ignorados
```
