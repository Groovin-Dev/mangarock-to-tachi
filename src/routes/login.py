import requests
import json

# Login using a provided email and password and return the user object. Most important thing in the user object is the idToken which is used for future requests


def login(email: str, password: str) -> dict:
    response = requests.post('https://www.googleapis.com/identitytoolkit/v3/relyingparty/verifyPassword?key=AIzaSyCFJPh6357HhIID3SgeRam2Cv6n139ymig',
                             headers={
                                 "Referer": "https://mangarock.com/account/login"},
                             data={"email": email, "password": password})

    content = json.loads(response.content)
    return content
