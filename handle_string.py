def handle_string(value):
    result = {'letters': 0, 'digits': 0}
    for c in value:
        if c.isalpha():
            result['letters'] += 1
        if c.isdigit():
            result['digits'] += 1
    return result

if __name__ == '__main__':
    string = 'Hello world! 123!'
    res = handle_string(string)
    print('Letters - {0} Digits - {1}'.format(res['letters'], res['digits']))
