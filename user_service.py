USER = {
    "email": "admin@gmail.com",
    "password": "admin123"
}


def validate_login(email, password):

    if email == USER["email"] and password == USER["password"]:
        return True

    return False