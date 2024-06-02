import requests

weather_info = requests.get("https://api.openweathermap.org/data/2.5/weather?lat=-33.865143&lon=151.209900&appid=7fd7eefeb1dc04c071716e91b1567e02&units=metric")
# print(weather_info)
# print(weather_info.json())
weather_info_json = weather_info.json()
temp = weather_info_json["main"]["temp"]
temp_max = weather_info_json["main"]["temp_max"]
temp_min = weather_info_json["main"]["temp_min"]
print(f"The Temperature in Sydney Currently: {temp}° C")
print(f"The Highest Temperature in Sydney today: {temp_max}° C")
print(f"The Lowest Temperature in Sydney today: {temp_min}° C")