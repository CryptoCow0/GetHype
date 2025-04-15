# sha1

import hashlib
import sys

def sha1_hash(text: str) -> str:
    '''computes the SHA-1 hash'''
    hash_object = hashlib.sha1(text.encode())
    with open('./Cracking/script2.txt', 'a') as file:
        file.write(hash_object.hexdigest())
    return hash_object.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(sha1_hash(password))
    else:
        print("Error: No input string provided.")