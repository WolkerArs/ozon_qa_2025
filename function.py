import requests


def get_tallest_hero(gender, job):

    if gender not in ['male', 'female'] or job not in ['yes', 'no']:
        print('Неверный запрос')
        return

    url = "https://akabab.github.io/superhero-api/api/all.json"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Ошибка {response.status_code}")
        return

    heroes = response.json()
    max_height = 0
    result_hero = None

    if job == 'yes':
        has_job = True
    else:
        has_job = False

    for hero in heroes:

        if hero["appearance"]["gender"].lower() != gender:
            continue

        occupation = hero["work"]["occupation"]
        if occupation in ["-", "none", "unemployed", "", " "]:
            is_employed = False
        else:
            is_employed = True

        if is_employed != has_job:
            continue

        height_cm = hero["appearance"]["height"][1]

        if "cm" in height_cm:
            height_cm = float(height_cm.replace("cm", ""))
        elif "meters" in height_cm:
            height_cm = float(height_cm.replace("meters", "")) * 100
        else:
            continue

        if height_cm > max_height:
            max_height = height_cm
            result_hero = hero

    if result_hero:
        print(f'Самый высокий супергерой - {result_hero["name"]} '
              f'с ростом {result_hero["appearance"]["height"][1]}.')
        return result_hero
    else:
        print('Такого героя нет')
        return result_hero


if __name__ == "__main__":
    gender = input("Пол супергероя (male/female): ")
    job = input("Наличие работы (yes/no): ")
    get_tallest_hero(gender, job)
