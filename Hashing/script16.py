# GOST

from Crypto.Hash import GOST34112012
import sys

def gost_hash(text: str) -> str:
    '''computes the GOST R 34.11-2012 (Streebog) hash'''
    h = GOST34112012.new(data=text.encode())
    digest = h.hexdigest()
    with open('./Cracking/script16.txt', 'a') as file:
        file.write(digest)
    return digest

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(gost_hash(password))
    else:
        print("Error: No input string provided.")
