import requests

# OpenWeatherMap API-URL
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"
API_KEY = "YOUR_API_KEY_HERE"  # Wir werden das später eintragen

def get_weather(city):
    """
    Holt die aktuellen Wetterdaten für eine Stadt
    """
    params = {
        'q': city,
        'appid': API_KEY,
        'units': 'metric',  # Celsius
        'lang': 'de'  # Deutsche Beschreibung
    }
    
    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()  # Fehlerbehandlung
        return response.json()
    except requests.exceptions.ConnectionError:
        print("❌ Fehler: Keine Internetverbindung!")
        return None
    except requests.exceptions.HTTPError:
        print("❌ Fehler: Stadt nicht gefunden!")
        return None

def display_weather(data):
    """
    Zeigt die Wetterdaten schön formatiert an
    """
    if data is None:
        return
    
    city = data['name']
    country = data['sys']['country']
    temp = data['main']['temp']
    feels_like = data['main']['feels_like']
    humidity = data['main']['humidity']
    description = data['weather'][0]['description']
    wind_speed = data['wind']['speed']
    
    print("\n" + "="*50)
    print(f"🌍 Wetter in {city}, {country}")
    print("="*50)
    print(f"🌡️  Temperatur: {temp}°C (fühlt sich an wie {feels_like}°C)")
    print(f"☁️  Wetterlage: {description.capitalize()}")
    print(f"💧 Luftfeuchtigkeit: {humidity}%")
    print(f"💨 Windgeschwindigkeit: {wind_speed} m/s")
    print("="*50 + "\n")

def main():
    """
    Hauptfunktion
    """
    print("\n🌤️  Willkommen zur Weather App! 🌤️")
    print("-" * 50)
    
    if API_KEY == "YOUR_API_KEY_HERE":
        print("❌ Fehler: API-Key nicht gesetzt!")
        print("Bitte trage deinen OpenWeatherMap API-Key in main.py ein.")
        return
    
    while True:
        city = input("\n🏙️  Gib eine Stadt ein (oder 'exit' zum Beenden): ").strip()
        
        if city.lower() == 'exit':
            print("\n👋 Auf Wiedersehen!")
            break
        
        if not city:
            print("❌ Bitte gib eine Stadt ein!")
            continue
        
        data = get_weather(city)
        display_weather(data)

if __name__ == "__main__":
    main()
