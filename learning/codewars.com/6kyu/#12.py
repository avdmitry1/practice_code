def stock_list(list_of_art: list, list_of_cat: list):
    dict_of_cat = {}
    for cat in list_of_cat:
        dict_of_cat[cat] = 0
    for art in list_of_art:
        if art[0][0] in dict_of_cat:
            dict_of_cat[art[0][0]] += int(art.split()[1])
        else:
            dict_of_cat.get(art[0][0], 0)
    res = ''
    for k, v in dict_of_cat.items():
        res += f'({k} : {v}) - '
    return res[:-3] if sum(dict_of_cat.values()) > 0 else ''
    
    

print(stock_list(["BBAR 150", "CDXE 515", "BKWR 250", "BTSQ 890", "DRTY 600"], 
                 ["A", "B", "C", "D"]))