import requests

client_ip = requests.get("https://api.ipify.org").text

class Infinite:

    def Create():
        while True:
            request = requests.get(f"https://ppng.io/{client_ip}-infinite")
            # do something will the request

if __name__ == "__main__":
    Infinite.Create()
