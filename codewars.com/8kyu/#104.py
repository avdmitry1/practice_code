def name_shuffler(str_):
    str_ = str_.split()
    str_.reverse()
    return ' '.join(str_)


print(name_shuffler('john McClane'))
