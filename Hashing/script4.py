import hashlib
import sys

def sha256_hash(text: str) -> str:
    '''computes the SHA-256 hash'''
    hash_object = hashlib.sha256(text.encode())
    with open('./Cracking/script4.txt', 'a') as file:
        file.write(hash_object.hexdigest())
    return hash_object.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(sha256_hash(password))
    else:
        print("Error: No input string provided.")
