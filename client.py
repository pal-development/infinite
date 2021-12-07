import requests
from datetime import date


today = date.today()
client_ip = requests.get("https://api.ipify.org").text

class Winvr:

    def Create():
        for i in range(50):
            date =  today.strftime("-%d-%m-%Y-%H-%M-%S")
            request = requests.get(f"https://ppng.io/{client_ip}{str(date)}")
            # do something will the request

if __name__ == "__main__":
    Winvr.Create()
