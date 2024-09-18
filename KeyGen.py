import random
import string

def generate_key(length: int = 8):
    alphabet = string.digits + string.punctuation #+ string.ascii_letters
    #commenting out letters inorder to change "password generator" into "key generator"
    key = ''.join(random.choice(alphabet) for i in range (length))
    return key

key = generate_key()
print("Your Key is: " + key)