def how_much_i_love_you(nb_petals):
    words = ['I love you', 'a little', 'a lot', 'passionately', 'madly', 'not at all']
    return words[nb_petals % 6 - 1]


print(how_much_i_love_you(12))
