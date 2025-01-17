import requests
from datetime import datetime


APP_ID = "b6921a0b"
API_KEY = "dccc6d2ca897b7d47f784f480ac910a2"
exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

sheety_username = "ander"
sheety_password = "ksdhjf23i94ksfdhg94"

GENDER = "male"
WEIGHT_KG = 96.5
HEIGHT_CM = 175.3
AGE = 29

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_input = input("Tell which exercise you did today?: ")

nutri_data = {
    "query": "Ran 2 miles and walked for 30 minutes",
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE,
}


response = requests.post(url=exercise_endpoint, json=nutri_data, headers=headers)
response.raise_for_status()
result = response.json()


### Sheet
sheety_endpoint = "https://api.sheety.co/b217f8e0f39db66936a76913cfe16f2c/myWorkouts/hoja1"

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")



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

    # Basic Authentication
    sheet_response = requests.post(
        sheety_endpoint,
        json=sheet_inputs,
        auth=(
            sheety_username,
            sheety_password,
        )
    )

    print(sheet_response.json())


