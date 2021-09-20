def num_conversion(number):

    hours = number // 60
    minutes = number % 60
    if hours <= 1 and minutes <= 1:
        print(str(hours) + " hour, " + str(minutes) + " minute.")
    elif hours <= 1 and minutes > 1:
        print(str(hours) + " hour, " + str(minutes) + " minutes.")
    else:
        print(str(hours) + " hours, " + str(minutes) + " minutes.")


num_conversion(133)
num_conversion(71)
