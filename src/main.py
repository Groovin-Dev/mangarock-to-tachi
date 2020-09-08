from routes.validate_user import validate_user
from routes.login import login
from routes.get_favorites import get_favorites


def main(email: str, password: str):
    userExists = validate_user(email)

    if userExists:
        print('user exists')
        user = login(email, password)
        id_token = user['idToken']

        get_favorites(id_token)
    else:
        print('user does not exist')


if __name__ == "__main__":
    email = input('What is your email? ')
    password = input('What is your password? ')
    main(email, password)
