def handle_numbers(number1, number2, number3):
    return len([i for i in xrange(number1, number2+1) if i % number3 == 0])

if __name__ == '__main__':
    print(handle_numbers(1, 10, 2))
