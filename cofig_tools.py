import sys


def makeUser1(user):
    if type(user) is not str:
        print("ERROR: wrong type for a user", repr(user))
        sys.exit(1)
    home = f"/home/{user})"
    privateKey = f"/{home}/.ssh/id_ed25519"
    publicKey = f"{privateKey}.pub"
    return dict(home=home, privateKey=privateKey, publicKey=publicKey)


def makeUser(user: str):
    home = f"/home/{user}"
    privateKey = f"/{home}/.ssh/id_ed25519"
    publicKey = f"{privateKey}.pub"
    return dict(home=home, privateKey=privateKey, publicKey=publicKey)