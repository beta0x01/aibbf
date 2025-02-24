users = {
    "admin": "admin"
}

def authenticate(username, password):
    return users.get(username) == password
