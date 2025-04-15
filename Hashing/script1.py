import hashlib
import sys
def md5_hash(text: str) -> str:
    '''computes the md5_hash'''
    hash_object = hashlib.md5(text.encode())
    return hash_object.hexdigest()

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(md5_hash(password))
    else:
        print("Error: No input string provided.")
