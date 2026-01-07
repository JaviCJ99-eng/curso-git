import bcrypt

password = b"secret_password_123" # Password must be in bytes
salt = bcrypt.gensalt()           # Generate a random salt
hashed_password = bcrypt.hashpw(password, salt)

# The hashed password (including the salt) can be stored in a database
print(hashed_password)