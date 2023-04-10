import requests
from bs4 import BeautifulSoup

url = "https://nba.hupu.com/players/chrispaul-1037.html"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.192 Safari/537.36"
}
resp = requests.get(url, headers=headers)
page = BeautifulSoup(resp.text, "html.parser")
div = page.find("div", attrs={"class": "font"})
information = div.find_all("p")
for informat in information:
    print(informat.text)  # .text拿到被标签标记的内容
