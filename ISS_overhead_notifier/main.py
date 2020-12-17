import requests
from datetime import datetime, timezone

MY_LAT = 1.352083
MY_LNG = 103.819839
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
#
# iss_position = (data['iss_position']['longitude'], data['iss_position']['latitude'])
#
# print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise =int(data['results']['sunrise'].split("T")[1].split(":")[0])
sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

print(sunrise, sunset)
time_now = datetime.now(timezone.utc)
print(time_now)