🌤️ Weather App

Eine Python-Anwendung, die aktuelle Wetterdaten für jede beliebige Stadt abruft und anzeigt.

## Features

- 🌍 Wetterdaten für jede Stadt weltweit abrufen
- 🌡️ Aktuelle Temperatur anzeigen
- 💧 Luftfeuchtigkeit und Windgeschwindigkeit
- 💬 Deutsche Wetterbeschreibungen
- ⚠️ Fehlerbehandlung für ungültige Eingaben

## Installation

### Voraussetzungen

- Python 3.7 oder höher
- pip (Python Package Manager)

### Schritt 1: Repository klonen

```bash
git clone https://github.com/emynaaa/weather-app.git
cd weather-app
```

### Schritt 2: Abhängigkeiten installieren

```bash
pip install -r requirements.txt
```

### Schritt 3: API-Key besorgen

1. Gehe zu https://openweathermap.org/api
2. Registriere dich kostenlos
3. Generiere einen API-Key
4. Öffne `main.py` und ersetze `YOUR_API_KEY_HERE` mit deinem API-Key

## Verwendung

```bash
python main.py
```

Dann gib eine Stadt ein und erhalte die aktuellen Wetterdaten!

Beispiel:
```
🏙️  Gib eine Stadt ein: Berlin
🌍 Wetter in Berlin, DE
==================================================
🌡️  Temperatur: 15°C (fühlt sich an wie 14°C)
☁️  Wetterlage: Leicht bewölkt
💧 Luftfeuchtigkeit: 65%
💨 Windgeschwindigkeit: 3.5 m/s
==================================================
```

## Technologien

- **Python 3** - Programmiersprache
- **requests** - HTTP-Bibliothek für API-Aufrufe
- **OpenWeatherMap API** - Wetterdaten-API

## Lizenz

Dieses Projekt ist Open Source und frei nutzbar.

## Autor

emynaaa

---

Viel Spaß mit der Weather App! 🌍
