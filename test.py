import bcrypt

password = "mypassword"

salt = bcrypt.gensalt()
hashed_password = bcrypt.hashpw(password.encode(), salt)

print(hashed_password)