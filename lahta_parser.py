from datetime import date, datetime, timedelta
from bs4 import BeautifulSoup
from selenium import webdriver
import urllib.request as req
import requests
from pprint import pprint
import json

tomorrow = date.today() + timedelta(days=1)
print(f"День поиска: {tomorrow}")

page_url = f"https://tickets.lakhta.events/event/23FA307410B1F9BE84842D1ABE30D6AB48EA2CF8/{tomorrow}"

def get_html_page():
    response = requests.get(page_url)
    with open("test.html", "w") as f:
        f.write(response.text)
    page = BeautifulSoup(response.text, 'html5lib')
    page_title = page.find('title')
    print(f"Заголовок: {page_title.string}")
    page_items = page.find_all('div', class_="times__item")
    print(page_items)


def get_api_token() -> str:
    url = "https://tickets.lakhta.events/api/token"
    headers = {
        "accept": "*/*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "cookie": "LAKHTA_CENTRE_ONLINE_TICKETS=8gamvnggh7i64hddnl51r92sst",
        "sec-ch-ua": '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',

        "sec-fetch-dest": "empty",
        "user-agent": "Mozilla/5.0",
        "referer": page_url,
        "sec-fetch-site": "same-origin",
        "sec-fetch-mode": "cors",
        "x-csrf-token": "ab6ee9d9b1eab86a14de2e064964b749",
        "x-requested-with": "XMLHttpRequest"
    }
    response = requests.get(url, headers=headers)
    data = response.json()
    pprint(data)
    token = data["response"]
    with open("token.txt", "w") as f:
        f.write(token)
    return token


def post_api():
    with open("token.txt", "r") as f:
        token = f.readline()

    print(f"from file {token=}")

    if token == '':
        token = get_api_token()

    print(f"from request {token=}")

    api_url = "https://tickets.lakhta.events/api/no-scheme"
    headers = {
        "accept": "application/json, text/plain, */*",
        "accept-encoding": "gzip, deflate, br, zstd",
        "accept-language": "u,en;q=0.9,sl;q=0.8,la;q=0.7,id;q=0.6,pt;q=0.5",
        "content-length": "51",
        "content-type": "application/json;charset=UTF-8",
        "cookie": "LAKHTA_CENTRE_ONLINE_TICKETS=8gamvnggh7i64hddnl51r92sst",
        "dnt": "1",
        "origin": "https://tickets.lakhta.events",
        "priority": "u=1, i",
        "referer": page_url,
        "sec-ch-ua": '"Chromium";v="130", "YaBrowser";v="24.12", "Not?A_Brand";v="99", "Yowser";v="2.5"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": '"macOS"',
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-origin",
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.0.0 YaBrowser/24.12.0.0 Safari/537.36",
    }
    body = {
        "token": token
    }
    response = requests.post(api_url, headers=headers, data=body)
    if response.status_code == 200:
        # pprint(response.content)
        # pprint(response.json())
        with open("api_reponse.json", "w") as f:
            f.write(json.dumps(response.json()))
    else:
        print("something wrong")


post_api()
# get_api_token()





