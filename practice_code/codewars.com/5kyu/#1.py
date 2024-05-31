def domain_name(url: str):
    to_remove = ['http://', 'https://', 'www.']
    for i in to_remove:
        if i in url:
            url = url.replace(i, '')
    
    for i, v in enumerate(url):
        if '.' in url:
            if v == '.':
                url = url[:i]
    
    return url


print(domain_name('http://codewars'))
print(domain_name("icann.org"))
