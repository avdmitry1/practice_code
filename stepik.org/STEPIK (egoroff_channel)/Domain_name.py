def domain_name(url: str) -> str:
    result = url.replace('http://', '').replace('www.', '').replace('https://', '')
    result = result.split('.')
    return result[0]


print(domain_name("https://www.asos.com"))
