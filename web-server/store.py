import requests

def get_categories():
    r = requests.get('https://api.escuelajs.co/api/v1/categories')
    print('*'*8, 'estado de la peticion', '*'*8)
    print(r.status_code)
    print('*'*8, 'datos obtenidos en texto', '*'*8)
    print(r.text)
    print('*'*8, 'tipo de dato obtenido', '*'*8)
    print(type(r.text))

    print('*'*8, 'categorias', '*'*8)
    categories = r.json()
    for category in categories:
        print(category['name'])


