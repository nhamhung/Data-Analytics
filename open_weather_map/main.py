import requests
import os
from twilio.rest import Client

OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
lat, long, api_key = 1.290270, 103.851959, "2ace5a6d0d46347d31e40d48e598e45f"
account_sid = "AC5445f48d0268120d008a52e58253304b"
auth_token = "d75d9155e5daeb5987bf7fbd8fcc831b"

parameters = {
    "lat": lat,
    "lon": long,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}


response = requests.get(OWM_endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data['hourly'][:12]
weather_id_list = [hour['weather'][0]['id'] for hour in hourly_data]

if any(id < 600 for id in weather_id_list):
    client = Client(account_sid, auth_token)
    message = client.messages \
                .create(
                     body="It's going to rain today. Remember to bring an ☂️",
                     from_='+19362373772',
                     to='+6591608840'
                 )
    print(message.status)