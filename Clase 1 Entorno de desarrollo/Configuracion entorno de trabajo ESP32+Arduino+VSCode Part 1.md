
# 💡 Clase 1: Configuración del entorno de trabajo ESP32+Arduino+VSCode Part 1
Este instructivo te guiará paso a paso para configurar el entorno de desarrollo y cargar un programa sencillo en tu ESP32. El objetivo es encender el LED conectado al **pin GPIO 2**.

---

## 🧰 Requisitos

- Placa **ESP32 (modelo WROOM-DA Module)**
- **Cable USB** para conexión a la PC
- **Conexión a internet** para instalar librerías

---

## 🪛 Pasos de instalación y configuración


## 📹 Video con la clase completa:

Aqui puedes ver la clase completa en formato video o bien puedes seguir el instructivo paso a paso que se ve a continuación:


<a href="https://www.youtube.com/watch?v=7wvwOm2fLFk" target="_blank">
  <img src="https://github.com/user-attachments/assets/0f50aed8-1239-45bd-84bc-30879cc10f85" width="505" height="286" alt="capturaMin" />
</a>

### 1️⃣ Descargar e instalar el IDE de Arduino

Descarga la versión **2.3.6 del IDE de Arduino** desde el sitio oficial:

🔗 [https://www.arduino.cc/en/software](https://www.arduino.cc/en/software)

Instálala según el sistema operativo de tu computadora.

---

### 2️⃣ Agregar soporte para placas ESP32

Sigue los pasos para agregar la tarjeta ESP32 desde el gestor de placas. El enlace oficial con instrucciones es:

🔗 [https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html](https://docs.espressif.com/projects/arduino-esp32/en/latest/installing.html)

Deberás copiar el siguiente **URL del gestor de tarjetas** y pegarlo en las preferencias del IDE:

```
https://raw.githubusercontent.com/espressif/arduino-esp32/gh-pages/package_esp32_index.json
```

---

### 3️⃣ Seleccionar la placa correcta

En el IDE de Arduino seleccina **ESP32 WROOM DA MODULE**. Asegúrate también de seleccionar el **puerto COM** correcto donde esté conectado tu ESP32.

---

## 🧪 4️⃣ Compilar y cargar el siguiente demo

Este código enciende de manera permanente el LED conectado al **pin GPIO 2**.

```cpp
void setup() {
  // Configura el pin 2 como salida y lo enciende
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);
}

void loop() {
  // No es necesario repetir ninguna acción
}
```

---

### 5️⃣ Cargar el programa y verificar

Presiona el botón **"Subir"** en el IDE para cargar el programa a la placa.

✔️ Si todo está correcto, verás encenderse el LED conectado al **pin 2** del ESP32.

<img src="https://github.com/user-attachments/assets/92565322-2e7e-441b-814a-b0836014f77c" width="280" height="230" alt="Imagen ESP32 LED AZUL" />


---
