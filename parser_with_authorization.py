import requests
from bs4 import BeautifulSoup

LOGIN_URL = "http://130.193.59.87/login/"

if __name__ == "__main__":
    session = requests.session()
    response = session.get(LOGIN_URL)
    response.encoding = "utf-8"
    soup = BeautifulSoup(response.text, "lxml")
    token = soup.find("input", {"name": "csrfmiddlewaretoken"})
    data = {
        "username": "test_parser_user",
        "password": "testpassword",
        "csrfmiddlewaretoken": token["value"],
    }
    response = session.post(LOGIN_URL, data=data)
    response.encoding = "utf-8"
    print(response.text)
