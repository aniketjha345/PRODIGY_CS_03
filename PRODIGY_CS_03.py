# Password Complexity Checker
import re

# Password must be at least 8 character long.
password = input("Enter Your Password: ")
if len(password) < 8:
    print("Password must be at least 8 charcters long.")
# Password must contain one uppercase letter.
elif not re.search("[A-Z]", password):
    print("Password must contain at least one uppercase.")
# Password must contain one lowercase letter.
elif not re.search("[a-z]", password):
    print("Password must contain one lowercase letter.")
# Password must contain at leat one number.
elif not re.search("[0-9]", password):
    print("Password must contain at leat one number.")
# Password must contain at least one special character.
elif not re.search("[!\"#$%&\'()*+,\-./:;<=>?@[\\]^_`{|}~]", password):
    print("Password must contain at least one special character.")
else:
    print("Password is Strong")