import requests
from datetime import date

clients_ip = "" ## client to connects ip address (public)
today = date.today()

class Infinite:

    def Create():
        for i in range(50):
            date =  today.strftime("-%d-%m-%Y-%H-%M-%S")
            print(requests.get(f"https://ppng.io/{clients_ip}{str(date)}"))


if __name__ == "__main__":
    Infinite.Create()