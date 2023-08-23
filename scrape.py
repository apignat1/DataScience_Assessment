from urllib.request import urlopen
url = "https://en.wikipedia.org/wiki/List_of_natural_disasters_by_death_toll"
page = urlopen(url)
html_bytes = page.read()
html = html_bytes.decode("utf-8")
print(html)
