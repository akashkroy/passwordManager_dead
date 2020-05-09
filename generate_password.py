import random
import string

# length = int(input("Enter the length of password: "))

def gen_pass(length=8):
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    password = []
    for i in range(length):
        _ = random.choice(chars)
        password.append(_)
    print("".join(password))
     
if __name__=='__main__':
    gen_pass(10)