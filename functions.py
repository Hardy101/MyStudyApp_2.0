import werkzeug.security  # module for hashing Password


def hash_password(password):
    hashed_password = werkzeug.security.generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
    return hashed_password
