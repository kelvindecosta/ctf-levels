from argparse import ArgumentParser
from bs4 import BeautifulSoup
from country_converter import convert
from frontmatter import load
from json import dump
from mistune import markdown
from os import listdir, makedirs, walk
from os.path import dirname, exists, isdir, isfile, join, relpath
from zipfile import ZipFile


def get_games():
    """Parses arguments to get absolute paths
    """
    parser = ArgumentParser(description="Generate files for CTF in FBCTF Format")
    parser.add_argument("games", metavar="games", type=str, nargs="+", help="game folders")

    args = parser.parse_args()
    return args.games


def get_level(directory):
    """Returns level data and attachments

    Arguments:
        directory {path} -- Absolute path of level

    Returns:
        (dict, list) -- A tuple of a dict and list
    """
    readme = load(join(directory, "README.md"))
    data = {}

    data["type"] = "flag"
    data["title"] = readme.get("title")
    data["active"] = False

    soup = BeautifulSoup(markdown(readme.content), "html.parser")
    d_tag = soup.find("h2", text="Description")
    data["description"] = soup.contents[soup.contents.index(d_tag) + 1].next_element.find("code").text

    data["entity_iso_code"] = convert(names=[readme.get("country")], to="ISO2")

    data["category"] = readme.get("tag").replace("-", " ").upper()

    data["points"] = readme.get("points")
    data["bonus"] = readme.get("bonus")
    data["bonus_fix"] = readme.get("bonus")
    data["bonus_dec"] = readme.get("decrement")

    data["flag"] = readme.get("flag")

    h_tag = soup.find("h2", text="Hint")
    data["hint"] = soup.contents[soup.contents.index(h_tag) + 1].next_element.find("code").text

    data["penalty"] = readme.get("penalty")

    data["attachments"] = []

    a_tag = soup.find("h2", text="Attachments")
    attachments = []
    if a_tag:
        for li in soup.contents[soup.contents.index(a_tag) + 1].next_element.find_all("li"):
            attachments.append(li.find("a").text)

    l_tag = soup.find("h2", text="Links")
    links = []
    if l_tag:
        for li in soup.contents[soup.contents.index(l_tag) + 1].next_element.find_all("li"):
            links.append(li.find("a").text)
    data["links"] = links

    return data, attachments


def main():
    for game in get_games():
        lvl_dir = join(game, "levels")
        lvl_data = []

        attach_dir = join(game, "attachments")
        categories = {}
        categories["categories"] = []
        categories["categories"].append({"category": "None", "protected": True})
        categories["categories"].append({"category": "Quiz", "protected": True})
        cats = set()

        for level in [join(lvl_dir, d) for d in sorted(listdir(lvl_dir))]:
            data, attachments = get_level(level)
            cats.add(data.get("category"))

            lvl_data.append(data)

            if len(attachments) > 0:
                if not exists(attach_dir):
                    makedirs(attach_dir)

                with ZipFile(f"{join(attach_dir, relpath(level, lvl_dir))}.zip", "w") as z:
                    for path in attachments:
                        abs_path = join(level, path)

                        if isfile(abs_path):
                            z.write(abs_path, relpath(abs_path, lvl_dir))
                        elif isdir(abs_path):
                            for root, _, files in walk(abs_path):
                                for file in files:
                                    z.write(join(root, file), relpath(join(root, file), lvl_dir))

        for c in cats:
            categories["categories"].append({"category": c, "protected": False})

        with open(join(game, "categories.json"), "w") as f:
            dump(categories, f, indent=4)

        with open(join(game, "levels.json"), "w") as f:
            dump({"levels" : lvl_data}, f, indent=4)


if __name__ == "__main__":
    main()
