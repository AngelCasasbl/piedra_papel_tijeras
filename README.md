# Piedra, Papel o Tijeras

¡Bienvenido al clásico juego de **Piedra, Papel o Tijeras** en Python! Este proyecto te permite jugar contra la computadora al mejor de 3 rondas. El juego termina en cuanto uno de los jugadores gana 2 rondas.

---

## 🔧 Características del Juego
- **Interactividad:** Puedes elegir entre `piedra`, `papel` o `tijeras` en cada ronda.
- **Sistema de puntuación:** Gana el primer jugador que obtenga 2 victorias.
- **Elección aleatoria:** La computadora selecciona su jugada de manera aleatoria.
- **Mensajes en tiempo real:** Te informa si ganaste, perdiste o empataste cada ronda, además de mostrar el puntaje actual.

---

## 🔄 Reglas del Juego
1. **Piedra** vence a **Tijeras** (la rompe).
2. **Tijeras** vence a **Papel** (lo corta).
3. **Papel** vence a **Piedra** (lo envuelve).
4. En caso de empate (ambos eligen lo mismo), la ronda no otorga puntos y se repite.
5. Gana el primero en alcanzar **2 victorias**.

---

## 📄 Cómo Jugar

1. **Ejecuta el programa:** Asegúrate de tener Python instalado en tu sistema.
2. **Ingresa tu elección:** Escribe `piedra`, `papel` o `tijeras` cuando se te pida.
3. **Mira los resultados:** El programa te dirá quién ganó la ronda y mostrará el puntaje actualizado.
4. **Sigue jugando:** El juego termina tan pronto como alguien gana 2 rondas.

### Ejemplo de Flujo del Juego
```text
Elige piedra, papel o tijeras: piedra
La computadora eligió: tijeras
¡Ganaste esta ronda!
Puntaje -> Jugador: 1, Computadora: 0

Elige piedra, papel o tijeras: papel
La computadora eligió: tijeras
La computadora ganó esta ronda.
Puntaje -> Jugador: 1, Computadora: 1

Elige piedra, papel o tijeras: tijeras
La computadora eligió: papel
¡Ganaste esta ronda!
¡Felicidades! Ganaste el juego.
```

---

## 🛠️ Configuración y Ejecución

### Prerrequisitos
- Tener instalado **Python 3.6** o superior.

### Instrucciones
1. Clona este repositorio:
   ```bash
   git clone https://github.com/angelcasasbl/piedra-papel-tijeras.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd piedra-papel-tijeras
   ```
3. Ejecuta el programa:
   ```bash
   python piedra_papel_tijeras.py
   ```

---

## 🔄 Extensiones
Este proyecto es simple pero se puede extender. Algunas ideas:
- Agregar **modo multijugador** para jugar con un amigo.
- Incluir un **historial de rondas**.
- Diseñar una interfaz gráfica con bibliotecas como `tkinter` o `pygame`.
- Crear un **sistema de dificultad**, donde la computadora tenga estrategias más avanzadas.

---

## 📊 Estadísticas
- **Duración promedio de una partida:** 3 a 5 minutos.
- **Probabilidad de empate:** Depende de la suerte y las elecciones.

---

## 🚀 Contribuciones
Si deseas contribuir al proyecto, sólo sigue estos pasos:
1. Haz un fork del repositorio.
2. Crea una nueva rama para tus cambios.
3. Envía un pull request describiendo tu contribución.

---

## 🙏 Agradecimientos
Gracias por jugar este clásico reinventado en Python. ¡Espero que te diviertas!

