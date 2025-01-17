# make a request
import requests
import datetime as dt
import smtplib
import time

MY_LAT = 42.829320
MY_LNG = -1.654184

MY_EMAIL = "lafkjdsf"
MY_PASSWORD = "lasfghaklñhjsgo"

def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_longitude = float(data["iss_position"]["longitude"])
    iss_latitude = float(data["iss_position"]["latitude"])

    # Your position is within +5 or -5 degrees of the ISS position
    if MY_LAT <= iss_longitude + 5 and MY_LAT >= iss_longitude - 5 and MY_LNG <= iss_latitude + 5 and MY_LNG >= iss_latitude - 5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LNG,
        "formatted": 0,
    }

    response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
    # response = requests.get(url="https://api.sunrise-sunset.org/json?lat=42.829320&lng=-1.654184", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']['sunrise'].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = dt.datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look
# if up:
# BONUS: run the code every 60 seconds.
while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        connection = smtplib.SMTP("smtp.google.com")
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg="Subject:Look Up\n\nThe ISS is above you in the sky."
        )




