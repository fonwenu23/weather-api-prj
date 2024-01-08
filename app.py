import requests

api_key = 'f5c344aef27cad1a56eec11e09a33655'

user_input = input("Enter City: ")
weather_data = requests.get(
    f"https://api.openweathermap.org/data/2.5/weather?q={user_input}&units=imperial&APPID={api_key}")

weather = weather_data.json()['weather'] [0] ['icon']
temp = weather_data.json()['wind']['speed']

print(f"The weather in {user_input} is: {weather}")
print(f"The humidity is: {temp}")