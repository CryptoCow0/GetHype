import hashlib
import sys

def sha224_hash(text: str) -> str:
    '''computes the SHA-224 hash'''
    hash_object = hashlib.sha224(text.encode())
    return hash_object.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(sha224_hash(password))
    else:
        print("Error: No input string provided.")
