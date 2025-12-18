import requests
from bs4 import BeautifulSoup
url = "https://news.ycombinator.com"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
titles = soup.select("span.titleline > a")
print("=" * 60)
print("HACKER NEWS")
print("=" * 60)
for i, title in enumerate(titles[:10], 1):
    print(f"{i:2}. {title.text}")
    print(f"    {title.get('href')}")
    print()