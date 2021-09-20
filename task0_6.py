def get_max_number(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        return num1
    elif num2 > num1 and num2 > num3:
        return num2
    else:
        return num3


max_number = get_max_number(5, 88, 155)
print(max_number)
