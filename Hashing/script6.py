import hashlib
import sys

def sha512_hash(text: str) -> str:
    '''computes the SHA-512 hash'''
    hash_object = hashlib.sha512(text.encode())
    hex_digest = hash_object.hexdigest()
    with open('./Cracking/script6.txt', 'a') as file:
        file.write(hex_digest + '\n')
    return hex_digest

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(sha512_hash(password))
    else:
        print("Error: No input string provided.")
