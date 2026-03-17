import string

import string

def validate_password(password):
    return (
        len(password) >= 8 and
        any(char in string.ascii_lowercase for char in password) and
        any(char in string.ascii_uppercase for char in password) and 
        any(char in string.punctuation for char in password)
    )
is_valid = validate_password("@Mypassword1234")

text = "Tayo"
print(text.replace(' ', ' '))

print ("Is the Password valid?", is_valid)