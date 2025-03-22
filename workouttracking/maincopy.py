import requests
import os
from datetime import datetime

GENDER = "MALE"
WEIGHT_KG = 60
HEIGHT_CM = 160
AGE = 21

os.environ["APP_ID"] = "6bd62ccb"
APP_ID = os.environ.get("APP_ID")
#APP_ID = "6bd62ccb"
os.environ["API_KEY"] = "edcf54f9612d9b60cd0233cc3c1833a6"
API_KEY = os.environ.get("API_KEY")
#API_KEY = "edcf54f9612d9b60cd0233cc3c1833a6"
os.environ["sheety_endpoint"] = "https://api.sheety.co/8f0c843c74a249be94b6c2e0a1d0b8d6/workoutTracking/sheet1"
sheety_endpoint = os.environ.get("sheety_endpoint")
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
#sheety_endpoint = "https://api.sheety.co/8f0c843c74a249be94b6c2e0a1d0b8d6/workoutTracking/sheet1"

#USER_NAME = "shivv4m"
#PASSWORD = "Shivam@2004"
os.environ["USER_NAME"] = "shivv4m"
os.environ["PASSWORD"] = "Shivam@2004"
USER_NAME = os.environ.get("USER_NAME")
PASSWORD = os.environ.get("PASSWORD")

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_done = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=exercise_done, headers=headers)
result = response.json()


today = datetime.today().strftime("%d-%m-%Y")
now = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "sheet1":{
            "date": today,
            "time": now,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheet_response = requests.post(url=sheety_endpoint, json=sheet_inputs, auth=(USER_NAME, PASSWORD))
print(sheet_response.text)