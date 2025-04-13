import requests

def get_codewars_user(username: str) -> dict | None:
    url = f"https://www.codewars.com/api/v1/users/{username}"
    response = requests.get(url)

    if response.status_code == 200:
        return True
    else:
        print(f"Ошибка: {response.status_code} — {response.text}")
        return False
