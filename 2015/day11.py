#!/usr/local/bin/python3

def increasing_straight(index, item, password):
    if ord(password[index + 2]) - ord(password[index + 1]) != 1:
        return False
    if ord(password[index + 1]) - ord(item) != 1:
        return False
    return True

def has_two_pairs(password):
    pairs = 0
    while len(password) > 1:
        cur_char = password[0]
        if cur_char == password[1]:
            pairs += 1
            if pairs > 1:
                return True
            password = password[2:]
        else:
            password = password[1:]
    return False

def is_valid(password):
    if any(banned_letter in password for banned_letter in {'i', 'o', 'l'}):
        return False
    if not any(
            increasing_straight(index, item, password)
            for index, item in enumerate(password[:-2])):
        return False
    if not has_two_pairs(password):
        return False
    return True

def increment_password(password):
    incremented_char = ord(password[-1]) + 1
    if incremented_char > 122:
        incremented_char = 97
        return increment_password(password[:-1]) + chr(incremented_char)
    return password[:-1] + chr(incremented_char)

def generate_new_password(password):
    while True:
        password = increment_password(password)
        if is_valid(password):
            break
    return password

# assert not is_valid('hijklmmn')
# assert not is_valid('abbceffg')
# assert not is_valid('abbcegjk')
# assert generate_new_password('abcdefgh') == 'abcdffaa'
# assert generate_new_password('ghijklmn') == 'ghjaabcc'
s = 'hepxcrrq'
print('Generating new password for:', s)
print(generate_new_password(s))

s = 'hepxxyzz'
print('Generating new password for:', s)
print(generate_new_password(s))
