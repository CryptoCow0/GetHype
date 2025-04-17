import hashlib
import sys

def sha384_hash(text: str) -> str:
    '''computes the SHA-384 hash'''
    hash_object = hashlib.sha384(text.encode())
    hex_digest = hash_object.hexdigest()
    with open('./Cracking/script5.txt', 'a') as file: 
        file.write(hex_digest + '\n')
    return hex_digest

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(sha384_hash(password))
    else:
        print("Error: No input string provided.")
