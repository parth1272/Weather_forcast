import requests
import smtplib


api_key = "f613f01a303e96ec3cb4f0665433058d"
Endpoint = "https://api.openweathermap.org/data/2.5/forecast"

w_parameters = {
    "lat": 21.299980,
    "lon": 77.521751,
    "appid": api_key,
    "cnt" : 4
}

response = requests.get(Endpoint, params=w_parameters)
response.raise_for_status()
weather_data = response.json()
print(weather_data["list"][0]["weather"][0]["id"])

will_rain = True
print("done")
for i in weather_data["list"]:
    condition = i["weather"][0]["id"]
    if int(condition) < 700:
       will_rain = True

if will_rain:

    print("bring umbrella.")

    mail_id = "parthambadkar2@gmail.com"
    passw = "vrhy jgrr tuac yiah"

    connection = smtplib.SMTP("smtp.gmail.com")
    connection.starttls()
    connection.login(user=mail_id, password=passw)
    connection.sendmail(from_addr=mail_id, to_addrs="parthambadkar127@gmail.com", msg="subject:Weather updates \n\n It's cloudy today, might be rain. bring umbrella")
    connection.close()

