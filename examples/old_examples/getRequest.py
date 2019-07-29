from urllib import request

google_response = request.urlopen("https://www.google.com")
wikipedia_response = request.urlopen("https://tr.wikipedia.org")

resp = google_response
print(google_response.code)
