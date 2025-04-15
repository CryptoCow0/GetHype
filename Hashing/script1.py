import hashlib
import sys

"""
To replicate other hashes:
    - change function to your specific hash
    - write to file
    - change functionality
    - easy peasy
    - scriptx with x being number the hash is in list
"""
def md5_hash(text: str) -> str:
    '''computes the md5_hash'''
    hash_object = hashlib.md5(text.encode())
    with open('./Cracking/script1.txt', 'a') as file:
        file.write(hash_object.hexdigest())
    return hash_object.hexdigest()



if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(md5_hash(password))
    else:
        print("Error: No input string provided.")
