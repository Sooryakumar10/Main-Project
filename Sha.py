import hashlib

sha_value = hashlib.sha256(b'text').hexdigest()
print(sha_value)

