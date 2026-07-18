"""
Utilidades para el detector de sueño con Teachable Machine.

Modulos:
    - cargar_modelo: Carga un modelo de Teachable Machine (.h5) y sus labels.
    - predecir: Ejecuta una prediccion con el modelo sobre una imagen.
    - img_to_tm_input: Convierte un frame RGB de OpenCV a input para el modelo.
    - hablar: Reproduce un mensaje de voz en un proceso separado (pyttsx3).
    - NotificadorSueno: Envía notificaciones de escritorio con anti-spam.
"""
import os
import sys
import shutil
import subprocess
import tempfile
import threading
import tf_keras as keras
import numpy as np
from PIL import Image
from plyer import notification
import time


def cargar_modelo(model_path, labels_path):
    """Carga un modelo de Teachable Machine y sus labels.

    Si la ruta contiene caracteres Unicode (ej. 'Algebra'), copia el modelo
    a un directorio temporal para evitar errores de decodificacion en Windows.
    """
    safe_path = model_path
    if any(ord(c) > 127 for c in model_path):
        safe_path = os.path.join(tempfile.gettempdir(), 'tm_model.h5')
        shutil.copy2(model_path, safe_path)
    model = keras.models.load_model(safe_path, compile=False)
    with open(labels_path, 'r') as f:
        labels = [line.strip() for line in f.readlines()]
    print(f'Modelo cargado: {model_path}')
    print(f'Clases: {labels}')
    return model, labels


def predecir(model, img_array, labels):
    """Hace prediccion con el modelo de TM.

    Retorna (clase, confianza) donde clase es el texto del label
    y confianza es un float entre 0 y 1.
    """
    prediction = model.predict(img_array, verbose=0)
    index = np.argmax(prediction[0])
    confianza = prediction[0][index]
    return labels[index], confianza


def img_to_tm_input(frame, target_size=(224, 224)):
    """Convierte un frame de OpenCV (RGB) a input para el modelo de TM.

    Redimensiona a 224x224 y normaliza los pixeles al rango [-1, 1]
    que es lo que espera Teachable Machine.
    """
    img = Image.fromarray(frame).resize(target_size)
    img_array = np.asarray(img, dtype=np.float32)
    if img_array.ndim == 3 and img_array.shape[2] == 3:
        img_array = np.expand_dims(img_array, axis=0)
        img_array = (img_array / 127.5) - 1.0
    return img_array


def hablar(mensaje):
    """Reproduce un mensaje de voz en un proceso separado.

    Usa pyttsx3 con la voz en espanol si esta disponible.
    Se ejecuta en un subprocess para no bloquear la camara.
    """
    script = (
        'import pyttsx3;'
        'e=pyttsx3.init();'
        'voices=e.getProperty("voices");'
        'spanish=[v for v in voices if "es" in v.id.lower() or "spanish" in v.name.lower()];'
        f'e.setProperty("voice", (spanish[0].id if spanish else voices[0].id));'
        'e.setProperty("rate",150);'
        f'e.say("{mensaje}");'
        'e.runAndWait()'
    )
    subprocess.Popen(
        [sys.executable, '-c', script],
        creationflags=subprocess.CREATE_NO_WINDOW
    )


class LocutorLoop:
    """Repite un mensaje de voz en loop mientras este activo.

    Uso:
        locutor = LocutorLoop()
        locutor.iniciar("No te duermas")  # empieza a repetir
        locutor.detener()                 # deja de repetir
    """

    def __init__(self):
        self._activo = threading.Event()
        self._hilo = None

    def _loop(self, mensaje):
        while self._activo.is_set():
            try:
                script = (
                    'import pyttsx3;'
                    'e=pyttsx3.init();'
                    'voices=e.getProperty("voices");'
                    'spanish=[v for v in voices if "es" in v.id.lower() or "spanish" in v.name.lower()];'
                    f'e.setProperty("voice", (spanish[0].id if spanish else voices[0].id));'
                    'e.setProperty("rate",150);'
                    f'e.say("{mensaje}");'
                    'e.runAndWait()'
                )
                p = subprocess.Popen(
                    [sys.executable, '-c', script],
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                p.wait(timeout=5)
            except Exception:
                pass
            time.sleep(1)

    def iniciar(self, mensaje):
        if self._hilo and self._hilo.is_alive():
            return
        self._activo.set()
        self._hilo = threading.Thread(target=self._loop, args=(mensaje,), daemon=True)
        self._hilo.start()

    def detener(self):
        self._activo.clear()


class NotificadorSueno:
    """Maneja notificaciones de escritorio sin spamear.

    Tiene un intervalo minimo entre notificaciones para evitar
    que se llene el centro de notificaciones del sistema.
    """

    def __init__(self, intervalo=10):
        self.ultima = 0
        self.intervalo = intervalo

    def enviar(self, mensaje, titulo='ALERTA DE SUEÑO'):
        ahora = time.time()
        if ahora - self.ultima < self.intervalo:
            return
        try:
            notification.notify(
                title=titulo,
                message=mensaje,
                app_name='Detector de Sueno',
                timeout=10
            )
            self.ultima = ahora
            print(f'NOTIFICACION: {titulo} - {mensaje}')
        except Exception as e:
            print(f'Error notificacion: {e}')
