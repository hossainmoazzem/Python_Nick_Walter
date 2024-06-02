import requests


class Weather:
    def __init__(self, lat, lon, units = "metric"):
        self.lat = lat
        self.lon = lon
        self.units = units

weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?{self.lat}&{self.lon}&appid=7fd7eefeb1dc04c071716e91b1567e02&units=metric")
# print(weather_info)
weather_info_json = weather_info.json()
temp = weather_info_json["main"]["temp"]
print(temp)
# print(weather_info)
# print(weather_info.json()) 



my_city = Weather(self.lat,self.lon)
