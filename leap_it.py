#  This program tests if year entered is leap year or not

def leap_it(year):

    valid_output = "It is a leap year"

    year_string = str(year)

    if year % 4 == 0 and year_string[-2:] != "00":
        return print(valid_output)

    elif year_string[-2:] == '00' and year % 400 == 0:
        return print(valid_output)

    else:
        print("not a leap year", end="")


leap_it(2000)
