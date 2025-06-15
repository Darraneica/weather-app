import requests

def get_weather(city,state, API_KEY):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city},{state},US&appid={API_KEY}&units=metric"

    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        return {
            'city': data['name'],
            'state': state,
            'temperature': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description']
        }
    except requests.RequestException:
        return None
    
