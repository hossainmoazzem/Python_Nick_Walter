import requests #imports requests library in ordet to use requests.get() function to fetch data from weather API


# Create a class named City, for the City Class you would like to ask for Name of the city, Latitude and Longitude of the City also units of weather , make it default "metric", so it prints temperature as °C
# https://www.degreesymbol.net/ [go to this url to get the degree ° symbol]
 
class City:
    def __init__(self, name, lat, lon, units = "metric"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data() # this function gets data from API, Converts it to JSON format

    def get_data(self):
        weather_info = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={self.lat}&lon={self.lon}&appid=7fd7eefeb1dc04c071716e91b1567e02&units={self.units}")
        weather_info_json = weather_info.json()
        self.temp = weather_info_json["main"]["temp"]
        self.temp_max = weather_info_json["main"]["temp_max"]
        self.temp_min = weather_info_json["main"]["temp_min"]

        
    def temp_print(self):
        units_symble = "Celsius" # decleared a variable for units. using a simple if condition gave an option to user to get metric = Celsius [set default in init function] or imperial = Fahrenheit
        if self.units == "imperial":
           units_symble = "Fahrenheit"

        print(f"The Temperature in your city Currently: {self.temp}° {units_symble}")
        print(f"The Highest Temperature in your city today: {self.temp_max}° {units_symble}")
        print(f"The Lowest Temperature in your city today: {self.temp_min}° {units_symble}")
        print("-------------------------------------------------------")





London = City("London",51.509865,-0.118092,"imperial")
London.temp_print()

Sydney = City("Sydney",-33.968109,151.104080,"")
Sydney.temp_print()

Dhaka = City("Dhaka",23.822350,90.365417)
Dhaka.temp_print()


