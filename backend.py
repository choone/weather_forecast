import requests

def get_data(place,forecast_days=None):
    API_KEY ="d36403e6f02debcffddb30367d080f69"
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data["list"]
    nr_values = 8*forecast_days
    filtered_data = filtered_data[:nr_values]
    return filtered_data
