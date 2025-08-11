from bcrypt import checkpw, hashpw, gensalt


def build_hash_password(password: str, salt: int = 10) -> str:  # This function hashes passwords.
    password = password.encode("utf-8")
    hash_salt = gensalt(salt)
    password = hashpw(password, hash_salt)
    return password.decode("utf-8")


def p2_equal_p1(p2: str, p1_hashed: str) -> bool:  # This function check password2 is equal to password.
    p1_hashed = p1_hashed.encode("utf-8")
    p2 = p2.encode("utf-8")

    try:
        if checkpw(p2, p1_hashed):
            return True
        else:
            return False
    except ValueError:
        return False
