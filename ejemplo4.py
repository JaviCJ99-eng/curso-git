import bcrypt

password = b"secret_password_123" # Password must be in bytes
salt = bcrypt.gensalt()           # Generate a random salt
hashed_password = bcrypt.hashpw(password, salt)

# The hashed password (including the salt) can be stored in a database
#print(hashed_password)

pass1 = bcrypt.hashpw("cristianCrack".encode(), bcrypt.gensalt())
pass2 = bcrypt.hashpw("cristianCrack4".encode(), bcrypt.gensalt())
pass3 = b'$2b$12$V6BAjoezeFWJyOY8uBJHvOWlWravkFJHSJ4l2kXhIwoXdCRMlLnL6'
print(pass1)
print(pass2)
print(pass3)

print(bcrypt.checkpw("cristianCrack".encode(), pass3))