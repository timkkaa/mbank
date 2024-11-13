from django.contrib.sites import requests


def get_kgs_to_usd():
    api_key = 'a8MNZkB1j5fUoeGAkWGrQ1EksyZf31LygVK4tNSM9b50449c'

    # URL для получения курса с сомов на доллары
    url = f'https://api.fx.kg/v1/convert/KGS/USD'

    # Заголовки с API-ключом
    headers = {
        'Authorization': f'Bearer {api_key}',
    }

    # Отправляем запрос
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        return data  # Возвращаем полученные данные
    else:
        print(f"Ошибка: {response.status_code}")
        return None


rate = get_kgs_to_usd()
if rate:
    print(f"1 KGS = {rate['rate']} USD")
