import random
import string

def generate_password(length):
  all_characters = string.ascii_letters + string.digits + string.punctuation
  if length < 8:
    print("password length should be at least 8 characters.")
    return None
  passward = ''.join(random.choice(all_characters) for i in range(length))
  return password

print("Generated Password : ", generated_password(10))
