import hashlib
def md5_hash(text: str) -> str:
    '''computes the md5_hash'''
    hash_object = hashlib.md5(text.encode())
    return hash_object.hexdigest()

