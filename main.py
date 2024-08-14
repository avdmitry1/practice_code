tables = {
    1: {'name': 'Andrey', 'is_vip': True},
    2: None,
    3: None,
    4: None,
    5: {'name': 'Vasiliy', 'is_vip': False},
    6: None,
    7: None,
    8: None,
    9: None,
}

def is_table_free(table: int) -> bool:
    return tables[table] is None

def reserve_table(num: int, name: str, status: bool = True):
    if is_table_free(num):
        tables[num] = {'name': name, 'is_vip': status}
        
def delete_reservation(num: int):
    tables[num] = None
    
print(tables)
reserve_table(3, 'Gena', True)
reserve_table(4, 'Artem', False)
reserve_table(5, 'Artur', True)  # Артур не должен занять место Василия
print(tables)