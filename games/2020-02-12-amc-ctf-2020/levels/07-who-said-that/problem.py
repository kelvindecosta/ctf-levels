from Crypto import Random
from Crypto.PublicKey import RSA
from os import makedirs
from os import path
from random import randrange

from script import load_keys, encrypt, decrypt, sign, verify


def generate_keys(directory):                                                   # Generates RSA public and private keys and stores them in a directory
    random_generator = Random.new().read
    key = RSA.generate(2048, random_generator)
    prv_key, pub_key = key.export_key("PEM"), key.publickey().exportKey("PEM")

    with open(path.join(directory, "pub.pem"), "wb") as pub_f:                  # Save public key
        pub_f.write(pub_key)

    with open(path.join(directory, "prv.pem"), "wb") as prv_f:                  # Save private key
        prv_f.write(prv_key)


def random_pop(l):                                                              # Randomly remove an item from a list
    i = randrange(0, len(l))
    return l.pop(i)


if __name__ == "__main__":
    people = [
        "alice",
        "bob",
        "carol",
        "david",
        "eve",
        "frank",
        "grace",
        "homer",
        "ivan",
        "judy"
    ]
    

    if not path.exists("people"):                                               # Create public and private keys for each person
        for name in people:
            directory = path.join("people", name)
            makedirs(directory)
            generate_keys(directory)


    output = "message"
    if not path.exists(output):
        makedirs(output)

        sender = random_pop(people)                                             # Randomly choose sender
        recipient = random_pop(people)                                          # Randomly choose recipient

        snd_pub_key, snd_prv_key = load_keys(path.join("people", sender))       # Load keys of sender
        rcp_pub_key, rcp_prv_key = load_keys(path.join("people", recipient))    # Load keys of recipient

        
        flag = "CTF{k33p_y0ur_pr1v473_k3y5_54f3}"
        msg = str.encode(flag)                                                  # Encode flag before encryption
        cphr_txt = encrypt(msg, rcp_pub_key)                                    # Encrypt message with recipient's public key
        signature = sign(msg, snd_prv_key)                                      # Sign message with sender's private key
        
        with open(path.join(output, "encrypted.txt"), "wb") as f:               # Save cipher text
            f.write(cphr_txt)
        
        with open(path.join(output, "signature.crt"), "wb") as f:               # Save signature
            f.write(signature)