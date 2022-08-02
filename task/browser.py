import os
import sys
import requests
from bs4 import BeautifulSoup
from colorama import Fore


dir_name = sys.argv[1]

def create_dir(dir_name):
    try:
        os.mkdir(f'{dir_name}')
    except FileExistsError:
        print('Error: File already exists')

def user_request(url):
    if "." in url: page = url.split(".")[-2]
    if not url.startswith("http"):
        url = "https://" + url
        try:
            r = requests.get(url)
        except (requests.exceptions.ConnectionError, requests.exceptions.InvalidURL):
            print("Error: Incorrect URL")
            sys.exit(0)
        else:
            soup = BeautifulSoup(r.content, 'html.parser')
            for i in soup.find_all("a"):
                i.string = "".join([Fore.BLUE, i.get_text(), Fore.RESET])

            with open (f"{dir_name}\\{page}", "w") as f:
                reply = soup.get_text()
                print(reply)
                f.write(reply)



def task_execute():
    while (True):
        url = input()
        if url == "exit": break
        else: user_request(url)


def main():
    create_dir(dir_name)
    task_execute()


if __name__ == '__main__':
    main()
