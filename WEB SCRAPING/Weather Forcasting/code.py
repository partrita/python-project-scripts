import requests

city = input("\nEnter the city name : ")
url = f"https://wttr.in/{city}"
try:
    res = requests.get(url)
    print(res.text)
except requests.RequestException:
    print("Error occure Please try again later...")