import requests
from datetime import date
import os

clients_ip = "" ## client to connects ip address (public)
today = date.today()

class Infinite:

    def Create():
        for i in range(50):
            date =  today.strftime("-%d-%m-%Y-%H-%M-%S")
            os.system(f"echo 'pc_on_{date}' | curl -T - https://ppng.io/{clients_ip}{date}")


if __name__ == "__main__":
    Infinite.Create()
