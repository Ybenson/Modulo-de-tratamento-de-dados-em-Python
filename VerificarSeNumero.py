
def is_simple_number(value):
    if not value.strip().replace('-', '').replace('+', '').replace('.', '').isdigit():
        return False
    try:
         float(value)
    except ValueError:
         return False
    return True

print(is_simple_number("1234"))