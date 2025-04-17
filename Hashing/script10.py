import hashlib
import sys

def sha3_512_hash(text: str) -> str:
    '''computes the SHA-3-512 hash'''
    hash_object = hashlib.sha3_512(text.encode())
    hex_digest = hash_object.hexdigest()
    with open('./Cracking/script10.txt', 'a') as file:
        file.write(hex_digest + '\n')
    return hex_digest

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(sha3_512_hash(password))
    else:
        print("Error: No input string provided.")
