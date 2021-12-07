import requests
from datetime import date
import os

today = date.today()
client_ip = requests.get("https://api.ipify.org").text

class Infinite:

    def Create():
        for i in range(50):
            date =  today.strftime("-%d-%m-%Y-%H-%M-%S")
            os.system(f"echo 'pc_on_{date}' | curl -T - https://ppng.io/{client_ip}{date}")


if __name__ == "__main__":
    Infinite.Create()