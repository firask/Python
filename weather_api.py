import requests, json

apiKey = "3fda7ab8b6e746979ad36634e5ad830d"
baseURL = "https://api.openweathermap.org/data/2.5/weather?q="

CityName = input("Enter the City Name: ")

completeURL = baseURL + CityName + "&units=metric" +"&appid=" + apiKey

response = requests.get(completeURL)

data = response.json()

# print(data)

print("Current Temperature", data["main"]["temp"])
print("Feels Like Temperature", data["main"]["feels_like"])
print("Minimum Temperature", data["main"]["temp_min"])
print("Maximum Temperature", data["main"]["temp_max"])


