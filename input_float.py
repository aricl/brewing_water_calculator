def input_float(input_prompt) -> float:
    print(input_prompt, end='')
    try:
        user_input = input()
        float_value = float(user_input)
    except ValueError:
        print('Please enter a number of parts per million, e.g. 123.45')
        float_value = input_float(input_prompt)
        return float_value
    else:
        return float_value
