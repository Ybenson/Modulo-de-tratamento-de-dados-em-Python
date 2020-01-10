def validate_phone(phone):
    number = [numbers for numbers in phone]
    if (len(phone) == 8 or len(phone) == 9) and (number[0] == '7' or number[0] == '8'):
        return ('9' + phone)

    elif (len(phone) == 8 or len(phone) == 9) and phone.isnumeric():
        return phone
    else:
        return None

print(validate_phone("87777213"))

