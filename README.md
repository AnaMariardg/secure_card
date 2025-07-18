# 💳 Secure Card – Tokenized Card Prototype  

## 🇺🇸 English Version  
Cybersecurity educational project on **tokenization of sensitive payment card data**.  
Designed as a simple simulation to help understand how to better protect information without printing it.

---

### 🔍 Why this project?  
First step into cybersecurity. I created a simple payment card prototype with no printed data to protect seniors who still prefer physical cards over mobile wallets such as Apple Pay.  
**Goal?** Less cash, more privacy, no habit changes.

This helped me practice:  
- Python coding in real projects  
- Creating a modular file structure  
- Reading JSON data  
- Creating secure tokens with `hashlib`  
- Thinking about real-world security  

---

### ⚙️ How it works  
Each time you run the program, it generates a **unique token** (SHA-256 hash) using simulated card data.

#### 📁 Project Structure
secure_card/
├── main.py # Entry point
├── token/
│ └── generator.py # Token generator
├── utils/
│ └── helpers.py # JSON file reader
└── data/
└── card_data.json # Simulated card data

---

### Possible Attacks and Defenses

| Attack Type               | Suggested Defense                             |
|---------------------------|-----------------------------------------------|
| Token reuse               | Use one-time tokens                           |
| Data interception (MITM)  | Use HTTPS/TLS encryption                      |
| Physical card theft       | Add extra authentication (PIN, biometrics)    |
| Chip or hardware access   | Encrypt data inside the secure hardware       |

---

### Design Preview  
Check the card design preview in the folder: `assets/secure_card_design.png`.

---

# 💳 Tarjeta Segura – Prototipo educativo de tarjeta tokenizada  

## 🇪🇸 Versión en español  
Proyecto educativo en ciberseguridad sobre la **tokenización de datos sensibles en tarjetas de pago**.  
Diseñado como una simulación sencilla para comprender cómo proteger mejor la información sin imprimirla.

---

### ¿Por qué este proyecto?  
Este proyecto representa mi primer pequeño paso para crear algo propio en ciberseguridad.  
La idea nació al notar que muchos adultos mayores no se sienten cómodos con la tecnología moderna.  
Prefieren usar efectivo o tarjetas físicas en lugar de billeteras móviles como Apple Pay.  
Por eso decidí poner en práctica la tokenización creando un prototipo de tarjeta de pago sin información impresa.  

**Objetivos:**  
- Reducir el uso de efectivo  
- Aumentar la privacidad  
- Proteger contra fraudes visuales  
- Sin obligarlos a cambiar completamente sus hábitos

Este proyecto me ayudó a practicar:  
- Programación en Python  
- Organización modular de un proyecto real  
- Lectura de datos desde archivos JSON  
- Generación de tokens con `hashlib`  
- Pensamiento sobre seguridad práctica  

---

### ⚙️ ¿Cómo funciona?
Cada vez que se ejecuta el programa, se genera un **token único** (un hash SHA-256) usando los datos simulados de una tarjeta.

#### 📁 Estructura del proyecto
secure_card/
├── main.py # Punto de entrada del proyecto
├── token/
│ └── generator.py # Generación del token seguro
├── utils/
│ └── helpers.py # Función para leer el archivo JSON
└── data/
└── card_data.json # Datos simulados de la tarjeta

---

### Posibles ataques y mitigaciones

| Tipo de ataque               | Mitigación propuesta                          |
|------------------------------|-----------------------------------------------|
| Reutilización del token      | Usar tokens de un solo uso                    |
| Interceptación de datos (MITM) | Comunicación cifrada (HTTPS/TLS)           |
| Robo físico de la tarjeta    | Agregar PIN o biometría como capa extra       |
| Acceso al chip o hardware    | Cifrado fuerte dentro del hardware            |

---

### Vista del diseño  
La vista previa de la tarjeta se encuentra en la carpeta: `assets/secure_card_design.png`.

---

## About me / Sobre mí  
**Ana Maria Rodriguez Medina**  
MSc in Cybersecurity | BA in International Relations  
Passionate about Privacy, Cryptography & Digital Safety  
🇳🇮 Nicaragua  

---

## License / Licencia  
MIT – For educational use only.  
MIT – Solo para fines educativos. 