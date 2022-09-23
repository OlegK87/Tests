import requests

ya_token = ' '

def folder_creation(folder_name: str):
    url = f'https://cloud-api.yandex.net/v1/disk/resources/'
    headers = {'Content-Type': 'application/json',
                       'Authorization': f'OAuth {ya_token}'}
    params = {'path': f'{folder_name}',
                      'overwrite': 'false'}
    response = requests.put(url=url, headers=headers, params=params)

    return response.status_code

if __name__ == '__main2__':
    folder_creation()

