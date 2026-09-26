import bcrypt

def hash_password(password: str):
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(password.encode('utf-8'), salt).decode('utf-8')

def check_hash(password: str, hashed_pw: str):
    return bcrypt.checkpw(password.encode('utf-8'), hashed_pw.encode('utf-8'))
    
