from views.additions_calculator_view import view as additions_calculator_view
from views.profile_calculator_view import view as profile_calculator_view


def view():
    print(
        'Please select the mode you would like to use (1: additions from profile, '
        + '2: profile from additions): ',
        end=''
    )

    mode = input()

    try:
        integer_mode = int(mode)
    except ValueError:
        view()
    else:
        if integer_mode == 1:
            additions_calculator_view()
        elif integer_mode == 2:
            profile_calculator_view()
        else:
            view()
