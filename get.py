import requests

if __name__ == '__main__':
    url = 'http://httpbin.org/get'
    args = { 'nombre':'nico', 'curso':'python' }

    response = requests.get(url, params=args)
    print(response.url)

    if response.status_code == 200:
        content = response.content
        print(content)

        #print(response.content) # Imprimo en consola la página

        # Pasra guardar la página en un archivo html
        # content = response.content
        # file = open ('pagina.html', 'wb')
        # file.write(content)
        # file.close()

