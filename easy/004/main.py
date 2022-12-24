import secrets
import string


def generate_password(length=14):
    alphabet = string.ascii_letters + string.digits
    password = "".join(secrets.choice(alphabet) for _ in range(length))

    return password


if __name__ == "__main__":
    pw = generate_password()
    print(pw)
