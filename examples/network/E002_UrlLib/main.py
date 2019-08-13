import urllib.request

if __name__ == '__main__':
    URL = 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png'
    PATH = 'image.png'

    print("Sending request")
    urllib.request.urlretrieve(URL, PATH)
    print("Completed")
