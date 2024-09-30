def past(h, m, s):
    hours = h * 60 * 60 * 1000
    minutes = m * 1000 * 60
    seconds = s * 1000
    return hours + minutes + seconds


print(past(1, 0, 0))
