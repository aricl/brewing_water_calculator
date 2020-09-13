def input_concentration(input_prompt):
    print(input_prompt, end='')
    try:
        user_input = input()
        concentration = float(user_input)
    except ValueError:
        print('Please enter a number of parts per million, e.g. 123.45')
        concentration = input_concentration(input_prompt)
        return concentration
    else:
        return concentration
