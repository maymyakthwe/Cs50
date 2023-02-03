from fractions import Fraction
# turn fraction to percent
while True:
    try:
        fuel_left = round(Fraction(input("How much fuel left?")), 2)
        fuel_percent = fuel_left*100
        fuel_percent_str = str(fuel_percent)+"%"
    except ZeroDivisionError:
        pass
    except ValueError:
        pass
    else:
        # print result
        if fuel_percent <= 1:
            print("E")
            break
        if 1 < fuel_percent < 99:
            print(fuel_percent_str)
            break
        if 99 <= fuel_percent <= 100:
            print("F")
            break
