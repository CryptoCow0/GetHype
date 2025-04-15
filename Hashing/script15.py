import hashlib
import sys
import os

def blake2s_hash(text: str) -> str:
    '''computes the BLAKE2s hash'''
    hash_object = hashlib.blake2s(text.encode())
    with open('./Cracking/script15.txt', 'a') as file:
        file.write(hash_object.hexdigest())

    return hash_object.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(blake2s_hash(password))
    else:
        print("Error: No input string provided.")
