import requests
from bs4 import BeautifulSoup

response = requests.get("https://matchhistory.euw.leagueoflegends.com/en/#match-details/EUW1/4446458947/223316366")
content = response.content
soup = BeautifulSoup(content, 'lxml')

names = soup.find_all("div", id="main")

print(names)
