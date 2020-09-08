import requests
import json

# Validate users email and return if it exsits or not. Not really needed but it cleans things up a bit :)


def validate_user(email: str) -> int:
    response = requests.put(
        'https://mangarock.com/ajax/account/checkExistedUser', data={'email': email})

    content = json.loads(response.content)

    if "email" not in content['data'] or content['data']['email'] != email:
        return 0
    else:
        return 1
