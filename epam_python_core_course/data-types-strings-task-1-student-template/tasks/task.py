def get_fractions(a_b: str, c_b: str) -> str:
    ab = a_b.split('/')
    cb = c_b.split('/')
    res = f'{int(ab[0]) + int(cb[0])}/{ab[1] if ab[1] == cb[1] else int(ab[1]) + int(cb[1])}'
    return f'{a_b} + {c_b} = {res}' 
