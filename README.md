# 🎮 Joystick Input Reader – Thrustmaster Edition

Dieses Python-Projekt beschäftigt sich mit dem Auslesen von Hardware-Ausgaben. speziell vom **Thrustmaster-Joystick**, der über USB angeschlossen wird.

## 🧰 Ziel des Projekts

Ziel ist es, die **Eingabedaten des Joysticks** in Echtzeit auszulesen, zu analysieren und für mögliche Weiterverarbeitungen bereitzustellen. Dazu gehören:

- Position der Achsen (z. B. X, Y, Z, Schubregler)
- gedrückte Buttons
- D-Pad bzw. Hat-Switch

Langfristig kann das Projekt als Grundlage für Anwendungen in Bereichen wie **Simulation, Steuerungssysteme**, oder **Game-Entwicklung** dienen.

## ⚙️ Hardware

Das Projekt wurde mit einem **Thrustmaster T.Flight Stick X** getestet. Andere Joysticks mit standardisierter USB-Schnittstelle sollten ebenfalls funktionieren.

## 🐍 Technologie-Stack

- **Python 3.12**
- [pygame](https://www.pygame.org/) – zum Erfassen der Joystick-Eingaben

## 🚀 Erste Schritte

1. conda create -n hardware python=3.12
2. conda activate hardware
3. pip install black isort flake8 mypy pytest pandas sympy numpy pygame
4. Repository klonen:
   ```bash
   git clone https://github.com/dein-nutzername/joystick-reader.git
   cd joystick-reader

## notes
**black – Der Code Formatter**
Was es tut: Formatiert deinen Python-Code automatisch nach festen Regeln.

Ziel: Einheitlicher Stil im gesamten Code, keine Diskussionen über Leerzeichen oder Einrückungen.

Beispiel: Wandelt z. B. x= 1+2 in x = 1 + 2 um.

Nutzen: Spart Zeit bei Code-Reviews und sorgt für sauberen, gut lesbaren Code.
```bash
black .
```

**isort – Sortiert import-Anweisungen**
Was es tut: Sortiert deine import-Statements automatisch (Standardbibliothek, Drittanbieter, lokale Module).

Ziel: Aufgeräumte und logische Imports.

**flake8 – Statischer Code-Checker**
Was es tut: Überprüft deinen Code auf Verstöße gegen PEP 8, unbenutzte Variablen, überlange Zeilen, usw.

Ziel: Sauberer, korrekter Code ohne „Stolperfallen“.

Nutzen: Du findest Probleme schon beim Schreiben, nicht erst beim Debuggen.

**mypy – Statische Typprüfung**
Was es tut: Prüft deinen Code auf Typfehler, basierend auf deinen Typannotationen (str, int, list[str] etc.).

Ziel: Frühzeitiges Erkennen von Typ-Fehlverwendungen.

Beispiel: def foo(x: int) -> str: wird angemeckert, wenn int zurückkommt.

Nutzen: Mehr Sicherheit und Wartbarkeit bei größeren Projekten.

**pytest – Test-Framework**
Was es tut: Führt automatisierte Tests aus, erkennt test_*.py-Dateien und test_*-Funktionen.

Ziel: Testgetriebene Entwicklung (TDD) und kontinuierliche Absicherung der Funktionalität.

Nutzen: Du kannst jederzeit prüfen, ob alles noch funktioniert.