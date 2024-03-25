from passlib.context import CryptContext # this is for hashing the password

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto") # this is for hashing the password


def hash(password: str):
    return pwd_context.hash(password) # this is for hashing the password


"""
Here's how password verification works:
1. plain_password is the password input provided by the user. This is typically what the user enters in a password field on a login form.
2. hashed_password is the hashed version of the original password that was created when the user set or last changed their password. This is typically stored in a database.
3. pwd_context.verify(plain_password, hashed_password) is a method provided by the password hashing context object (pwd_context). This method takes the plain text password and the hashed password as arguments. It hashes the plain text password and compares it to the provided hashed password.
4. If the newly hashed plain text password matches the provided hashed password, the method returns True, indicating that the password is correct. If they do not match, it returns False, indicating that the password is incorrect.
This function is a crucial part of secure password handling in web applications. By comparing hashed versions of passwords, the system can verify user credentials without ever needing to store or directly handle plain text passwords.
"""

def verify(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password) # this is for hashing the password