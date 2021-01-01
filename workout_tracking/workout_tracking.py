import requests
from datetime import datetime
import os

APP_ID = os.environ['APP_ID']
API_KEY = os.environ['API_KEY']
exercise_api_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
spreadsheet_api_endpoint = os.environ['SHEET_ENDPOINT']
GENDER = "male"
WEIGHT = 67
HEIGHT = 168
AGE = 22

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

query_params = {
    "query": input("What exercises did you do today? "),
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(exercise_api_endpoint, json=query_params, headers=headers)
result = response.json()
# print(result)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

headers = {
    "Authorization": f"Basic {os.environ['AUTHORIZATION']}"
}

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(spreadsheet_api_endpoint, json=sheet_inputs, headers=headers)

    print(sheet_response.text)