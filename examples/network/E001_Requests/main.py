import requests

# Downloading image via requests library
if __name__ == '__main__':
    URL = 'https://github.githubassets.com/images/modules/logos_page/GitHub-Mark.png'

    print("Send request")
    file = requests.get(URL)

    print("Response taken")
    open('image.png', 'wb').write(file.content)

    print("Completed")
