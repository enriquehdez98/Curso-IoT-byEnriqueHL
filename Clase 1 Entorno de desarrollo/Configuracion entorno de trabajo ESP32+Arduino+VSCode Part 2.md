# Guía rápida para programar ESP32 con PlatformIO en VSCode

Sigue estos pasos para configurar tu entorno de desarrollo con PlatformIO y programar un ESP32 usando el framework de Arduino.

---

## 1. Instala Visual Studio Code

Descarga e instala VSCode desde su sitio oficial:  
🔗 [https://code.visualstudio.com](https://code.visualstudio.com)

---

## 2. Instala el plugin PlatformIO

Una vez abierto VSCode:

- Dirígete a la pestaña de extensiones (ícono de cuadrado en la barra lateral).
- Busca "PlatformIO IDE" e instálalo.

---

## 3. Crea un nuevo proyecto PlatformIO

1. Abre PlatformIO desde la barra lateral izquierda (ícono del alien).
2. Selecciona **"New Project"**.
3. Asigna un nombre a tu proyecto.
4. En el campo **Board**, selecciona:

   ```
   Espressif ESP32 Dev Module
   ```

5. Asegúrate de elegir el **Framework: Arduino**.
6. Haz clic en **Finish**.

---

## 4. Configura el archivo `platformio.ini`

Abre el archivo `platformio.ini` que se creó automáticamente y añade (o modifica) las siguientes líneas:

```ini
upload_port = COM9
upload_speed = 115200
monitor_speed = 115200
```

⚠️ Asegúrate de que `COM9` sea el puerto real donde está conectado tu ESP32. Puedes verificarlo desde el *Administrador de dispositivos* de Windows.

---

## 5. Escribe el código en `main.cpp`

Reemplaza el contenido del archivo `src/main.cpp` con el siguiente código:

```cpp
#include <Arduino.h>

#define LED_BUILTIN 2

void setup() {
  Serial.begin(115200);
  pinMode(LED_BUILTIN, OUTPUT);
  Serial.println("Hello, World!");
}

void loop() {
  Serial.println("LED is ON");
  digitalWrite(LED_BUILTIN, HIGH);
  delay(1000);

  Serial.println("LED is OFF");
  digitalWrite(LED_BUILTIN, LOW);
  delay(1000);
}
```

---

## 6. Compila, carga y monitorea

1. Haz clic en el icono de **check** para compilar el proyecto.
2. Haz clic en el icono de **flecha derecha (→)** para cargar el programa al ESP32.
3. Abre el **Monitor Serial** (Ctrl + Alt + M) para ver los mensajes enviados por el microcontrolador.

Deberías ver un mensaje tipo:

```
Hello, World!
LED is ON
LED is OFF
...
```

---

✅ ¡Listo! Has configurado correctamente tu entorno de desarrollo para el ESP32 usando PlatformIO y Arduino.
