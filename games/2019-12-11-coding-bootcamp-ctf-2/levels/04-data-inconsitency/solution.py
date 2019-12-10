import os
from bs4 import BeautifulSoup


def tokens(string):
    nums = list(map(ord, string))
    return max(nums) - min(nums)


if __name__ == "__main__":
    directory = "profiles"
    for filename in os.listdir(directory):
        filename = os.path.join(directory, filename)

        with open(filename, "r") as f:
            content = f.read()

        soup = BeautifulSoup(content, "html.parser")

        n = soup.find("title").text
        t = int(soup.find("strong").text)
        w = soup.find("a").get("href")

        if t != tokens(n):
            print("CTF{" + w + "}")
            exit()
