def validate_pin(pin):
    result = []
    for i in pin:
        if not i.isdigit():
            return False
        result.append(i)
    return True if len(result) == 4 or len(result) == 6 else False


print(validate_pin('-1234'))
