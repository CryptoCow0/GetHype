import hashlib
import sys

def sha224_hash(text: str) -> str:
    '''computes the SHA-224 hash'''
    hash_object = hashlib.sha224(text.encode())
    with open('./Cracking/script3.txt', 'a') as file:
        file.write(hash_object.hexdigest())
    return hash_object.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(sha224_hash(password))
    else:
        print("Error: No input string provided.")
