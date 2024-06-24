import requests
from pywebio.output import put_text
from pywebio import start_server


def fetch_astronauts():
    response = requests.get("http://api.open-notify.org/astros.json")
    data = response.json()
    astronauts = [astronaut['name'] for astronaut in data['people']]
    return astronauts


def fetch_users():
    response = requests.get("https://dummyjson.com/users")
    data = response.json()
    users = data['users']
    return users


def users_age_28(users):
    age_28_users = [user['firstName'] + ' ' + user['lastName'] for user in users if user['age'] == 28]
    return age_28_users


def main():
    # Part 1: List of astronauts
    astronauts = fetch_astronauts()
    put_text("Космонавти на орбіті зараз:")
    for astronaut in astronauts:
        put_text(astronaut)

    # Part 2: Users 28 years of age
    users = fetch_users()
    age_28_users = users_age_28(users)
    put_text("Користувачі віком 28 років:")
    for user in age_28_users:
        put_text(user)


if __name__ == '__main__':
    start_server(main, port=8080)
