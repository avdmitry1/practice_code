def get_word_indices(strings: list[str]):
    new_dict = {}
    for i, v in enumerate(strings):
        for j in v.lower().split():
            if j in v.lower():
                new_dict.setdefault(j, [])
                new_dict[j].append(i)
            else:
                new_dict.setdefault(j, [0])

    return new_dict


get_word_indices(['This is a string',
                  'test String',
                  'test',
                  'string'])

# {'look': [0], 'at': [0], 'my': [0, 1], 'horse': [0, 1], 'is': [2], 'amazing': [2]}
