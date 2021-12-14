from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import PKCS1_v1_5
from Crypto.Hash import SHA256
from os import path, listdir
import itertools


def load_keys(directory):                                               # Load RSA public and private keys from directory
    pub_file = path.join(directory, "pub.pem")
    prv_file = path.join(directory, "prv.pem")

    with open(pub_file, "rb") as f:
        pub_key  = RSA.importKey(f.read())
    
    with open(prv_file, "rb") as f:
        prv_key  = RSA.importKey(f.read())

    return pub_key, prv_key


def load_message(directory):                                            # Load cipher text and signature from directory
    c_file = path.join(directory, "encrypted.txt")
    s_file = path.join(directory, "signature.crt")

    with open(c_file, "rb") as f:
        cphr_txt  = f.read()
    
    with open(s_file, "rb") as f:
        signature  = f.read()

    return cphr_txt, signature


def encrypt(msg, pub_key):                                              # Encrypt message with a public key
    cipher = PKCS1_OAEP.new(pub_key)
    return cipher.encrypt(msg)


def decrypt(cphr_txt, prv_key):                                         # Decrypt cipher with private key
    cipher = PKCS1_OAEP.new(prv_key)
    return cipher.decrypt(cphr_txt)


def sign(msg, prv_key):                                                 # Sign message with private key
    signer = PKCS1_v1_5.new(prv_key)
    digest = SHA256.new()
    digest.update(msg)
    return signer.sign(digest)


def verify(msg, signature, pub_key):                                    # Verify message with public key
    signer = PKCS1_v1_5.new(pub_key)
    digest = SHA256.new()
    digest.update(msg)
    return signer.verify(digest, signature)


if __name__ == "__main__":
    """
    Was I God? No. Because God didn't win the war. We did.
    
    ---

    In asymmetric cryptography each user has two keys:

    *   A Public Key , distributed to everyone
    *   A Private Key, kept internally

    RSA public and private keys are nothing but very long numbers.

    When Public Key Cryptography is used :

    *   The sender encrypts the message with the recipient's public key
    *   The sender digitally signs the message with their private key
    *   The recipient decrypts the message with their private key
    *   The recipient verifies the message with the signature and the sender's public key
    """

    people = listdir("people")                                          # Load list of people
    cphr_txt, signature = load_message("message")                       # Load message
