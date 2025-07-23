import requests, bs4

url = "https://www.conestogac.on.ca"

res = requests.get(url)

soup = bs4.BeautifulSoup(res.text, 'html.parser')

page_links = soup.find_all('a')

for link in page_links:
    print(link.get('href'))