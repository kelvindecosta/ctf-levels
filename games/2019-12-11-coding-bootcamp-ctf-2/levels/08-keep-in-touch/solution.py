import re
import requests
from bs4 import BeautifulSoup


def wiki(title):
	"""Takes a title and wraps it to form a https://en.wikipedia.org URL
	Arguments:
		title {str} -- Title of Wikipedia Article
	Returns:
		{str} -- URL on wikipedia
	"""
	return f"https://en.wikipedia.org/wiki/{title}"



def get_pages(title):
	"""Returns a set of wikipedia articles linked in a wikipedia article
	Arguments:
		title {str} -- Article title
	Returns:
		{set()} -- A set of wikipedia articles
	"""
	response = requests.get(wiki(title))
	soup = BeautifulSoup(response.content, 'html.parser')
	links = soup.find_all('a', href=re.compile('^/wiki/[^.:#]*$'))
	pages = set([link.get('href')[len("/wiki/"):] for link in links])

	return pages


if __name__ == "__main__":
	print("CTF{" + str(len(get_pages("Erdős_number"))) + "}")
