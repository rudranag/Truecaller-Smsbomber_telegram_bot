import hashlib

def hash_string(string):
  # Encode the string as bytes
  string_bytes = string.encode()

  # Create a new SHA256 hash object
  hash_object = hashlib.sha256()

  # Update the hash object with the string data
  hash_object.update(string_bytes)

  # Get the hexadecimal representation of the hash
  hash_hex = hash_object.hexdigest()

  return hash_hex