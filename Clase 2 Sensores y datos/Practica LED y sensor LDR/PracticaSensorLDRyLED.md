# Práctica: Variar la intensidad de un LED usando un sensor LDR con ESP32

## 📋 Objetivo
Aprender a leer el valor de un **sensor LDR** y utilizarlo para variar la intensidad de un **LED** mediante **PWM (Modulación por Ancho de Pulso)** en el ESP32.

---

## 🛠 Materiales
- 1 x Placa ESP32
- 1 x Sensor LDR (Light Dependent Resistor)
- 1 x Resistencia de 10kΩ (para divisor de tensión)
- 1 x LED
- 1 x Resistencia de 330Ω (para limitar corriente del LED)
- Cables de conexión
- Protoboard

---

## 🔌 Conexiones

| Componente   | ESP32 Pin | Descripción              |
|--------------|-----------|--------------------------|
| LDR + 10kΩ   | GPIO34    | Lectura analógica (ADC1) |
| LED + 330Ω   | GPIO25    | Salida PWM               |
| GND común    | GND       | Tierra                   |
| VCC LDR      | 3.3V      | Alimentación del sensor  |

![Imagen conexiones ESP32](https://linuxhint.com/wp-content/uploads/2023/02/4-78.png)

📌 El LDR se conecta en **serie con la resistencia de 10kΩ** formando un divisor de tensión. El punto intermedio va al **GPIO34**.

---

## 📄 Código (PlatformIO / Arduino IDE)

```cpp
#include <Arduino.h>

int pinLDR = 34;    // Entrada analógica
int pinLed = 25;    // Salida PWM

// Configuración PWM para ESP32
const int canalPWM = 0;  // Canal PWM (0 a 15)
const int freqPWM = 5000; // Frecuencia en Hz
const int resolucion = 8; // Resolución de 8 bits (0-255)

void setup() {
  Serial.begin(115200);
  
  // Configuración de PWM
  ledcSetup(canalPWM, freqPWM, resolucion);
  ledcAttachPin(pinLed, canalPWM);

  Serial.println("Control de LED con LDR");
}

void loop() {
  // Leer valor analógico del LDR (0 - 4095 en ESP32)
  int valorLDR = analogRead(pinLDR);

  // Mapear valor de LDR a rango PWM (0 - 255)
  int brillo = map(valorLDR, 0, 4095, 0, 255);

  // Aplicar brillo al LED
  ledcWrite(canalPWM, brillo);

  // Mostrar valores en Serial
  Serial.print("LDR: ");
  Serial.print(valorLDR);
  Serial.print("  | Brillo PWM: ");
  Serial.println(brillo);

  delay(100);
}
```

**analogRead(pin)**

Lee un valor analógico desde un pin ADC (0 a 4095 en ESP32).

map(valor, in_min, in_max, out_min, out_max)

Convierte un valor de un rango a otro.
En este caso, pasamos de 0-4095 (ADC del ESP32) a 0-255 (PWM de 8 bits).

<br>

**PWM en ESP32**

ledcSetup(canal, frecuencia, resolucion) → Configura el canal PWM.

ledcAttachPin(pin, canal) → Asocia un pin al canal PWM.

ledcWrite(canal, dutyCycle) → Envía un valor de ciclo de trabajo (0-255 si es 8 bits).