import random
import string

def a_password(length):
    char=string.ascii_letters+string.digits+string.punctuation
    password=''.join(random.choice(char)for i in range(length))
    return password

password=a_password(10)
print("generated password is:",password)
