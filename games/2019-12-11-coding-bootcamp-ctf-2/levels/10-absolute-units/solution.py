import requests
from bs4 import BeautifulSoup


if  __name__ == "__main__":
    response = requests.get('https://historyfilms.co.uk')
    soup = BeautifulSoup(response.content, 'html.parser')
    tags = soup.findAll('strong')
    tags = [tag.text for tag in tags]
    print("CTF{" + str(len(set(tags))) + "}")
