import requests
from twilio.rest import Client

LAT = 42.816811
LON = -1.642819

OWM_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
api_key = "a6dc641d5b08be42de62e2f14e40f17f"

account_sid = "ladfjlñasjfañlsdhfjaklñdfhjsgñakldhjsfgklaj"
auth_token = 'your_auth_token'

weather_params = {
    "lat": LAT,
    "lon": LON,
    "appid": api_key,
    "exclude": "current,munutely,daily"
}

response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# print(weather_data["hourly"][0]["weather"][0]["id"])
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = weather_data["wather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an umbrella.")
    client = Client(account_sid, auth_token)
    massage = client.messages \
        .create(
        body="It's going to rain today. Remember to bring your umbrela.",
        from="+15065478616",
        to="+15558675310"
    )
    print(message.status)


print(weather_slice)
