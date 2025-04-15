import sys
import blake3

def blake3_hash(text: str) -> str:
    hash_object = blake3.blake3(text.encode())
    hash_hex = hash_object.hexdigest()
    with open('./Cracking/script13.txt', 'a') as file:
        file.write(hash_hex)
    return hash_hex

if __name__ == "__main__":
    if len(sys.argv) > 1:
        password = sys.argv[1]
        print(blake3_hash(password))
    else:
        print("Error: No input string provided.")
