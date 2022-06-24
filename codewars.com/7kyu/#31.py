def remove_url_anchor(url):
    index = url.find('#')
    return url[:index] if index >= 0 else url


print(remove_url_anchor("www.codewars.com#about"))
