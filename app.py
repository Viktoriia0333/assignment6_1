def calculate():
    try:
        a = float(input('First number:  '))
        b = float(input('Second number: '))
        operation = input('Operation: ')
        match operation:
            case '+':
                print(f'{a} + {b} = {a+b}')
            case '-':
                print(f'{a} - {b} = {a - b}')
            case '*':
                print(f'{a} * {b} = {a * b}')
            case _:
                print(f"I don`t know this operation yet")
    except ValueError:
        print('This is nor a valid number. Do not ruin my program')


calculate()
