def makeUser(user):
    home = f"/home/{user}"
    privateKey = f"/{home}/.ssh/id_ed25519"
    publicKey = f"{privateKey}.pub"
    return dict(home=home, privateKey=privateKey, publicKey=publicKey)


data = [
    makeUser("ivan"),
    makeUser("maxim"),
]
