import requests
import subprocess

clients_ip = input("CLIENTS IP: ") ## client to connects ip address (public)

class Infinite:

    def Create():
        for i in range(50):
            subprocess.getoutput(f"echo ping | curl -T - https://ppng.io/{clients_ip}-infinite")


if __name__ == "__main__":
    Infinite.Create()
