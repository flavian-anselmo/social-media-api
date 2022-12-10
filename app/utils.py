from passlib.context import CryptContext



pswd_conxt = CryptContext(schemes = ["bcrypt"],deprecated = "auto")


def verify_pswd(plain_pswd, hashed_pswd):
    # verify before hashing
    return pswd_conxt.verify(plain_pswd, hashed_pswd)

def get_pswd_hash(pswd):
    # hash of the password
    return pswd_conxt.hash(pswd)    
