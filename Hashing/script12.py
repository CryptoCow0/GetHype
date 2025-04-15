#blake2 

import hashlib
import sys

def blake2b_hash(text: str) -> str:
    '''computes the BLAKE2b hash'''
    hash_object = hashlib.blake2b(text.encode())
    with open('./Cracking/script12.txt', 'a') as file:
        file.write(hash_object.hexdigest())
    return hash_object.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(blake2b_hash(password))
    else:
        print("Error: No input string provided.")
