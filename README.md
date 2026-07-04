# Control por Gestos — Plantas y Puzzles

Aplicaciones interactivas que utilizan la cámara web y **MediaPipe Hands** para detectar gestos de la mano en tiempo real. Incluye una planta virtual que crece con los dedos y tres versiones de un puzzle de 3×3 controlado por gestos.

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
# Clonar el repositorio
git clone https://github.com/TU_USUARIO/TU_REPOSITORIO.git
cd TU_REPOSITORIO

# Instalar dependencias
pip install opencv-python mediapipe==0.10.14 numpy
```

> **Nota:** MediaPipe 0.10.14 es la versión recomendada para compatibilidad.

---

## Uso

Abre el notebook en Jupyter:

```bash
jupyter notebook "flores y mano.ipynb"
```

Ejecuta la celda del programa que quieras usar.

### Controles comunes
| Tecla  | Acción              |
|--------|---------------------|
| `ESC`  | Salir del programa  |
| `X`    | Cerrar ventana      |
| `ESPACIO` | Tomar foto (V2, V3) |
| `R`    | Reiniciar (V2, V3)  |

---

## Estructura del proyecto

```
python/
├── flores y mano.ipynb   # Notebook principal (4 programas)
├── README.md             # Este archivo
└── .gitignore            # Archivos ignorados
```
