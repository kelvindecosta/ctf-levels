import random
import string
import hashlib
import mistune
import os


def name():
    return "".join(random.choice(string.ascii_lowercase + string.digits) for _ in range(10))


def digest(string):
    m = hashlib.md5()
    m.update(str.encode(string))
    return m.digest().hex()


def html(profile):
    raw = f"""# {profile.get("name")}\n\nI have **{profile.get("tokens")}** tokens in my wallet\n\nPlease support me by sending blockchain based tokens [here]({profile.get("code")})"""
    return f"""<html lang="en">\n<head>\n\t<meta charset="UTF-8">\n\t<meta name="viewport" content="width=device-width, initial-scale=1.0">\n\t<title>{profile.get("name")}</title>\n</head>\n<body>\n{mistune.markdown(raw)}</body>\n</html>"""


def tokens(string):
    nums = list(map(ord, string))
    return max(nums) - min(nums)


if __name__ == "__main__":
    random.seed(42)

    profiles = {}
    for _ in range(1000):
        while True:
            n = name()
            if profiles.get(n) is None:
                profiles[n] = {}
                profiles[n]["name"] = n
                profiles[n]["tokens"] = tokens(n)
                profiles[n]["code"] = digest(n)
                break

    outlier = random.choice(list(profiles.keys()))
    profiles[outlier]["tokens"] = -1

    directory = "profiles"
    if not os.path.exists(directory):
        os.makedirs(directory)

    for k in profiles:
        p = profiles.get(k)
        filename = os.path.join(directory, f"""{p.get("name")}.html""")
        with open(filename, "w") as f:
            f.write(html(p))
