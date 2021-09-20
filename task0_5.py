def calc_area(num1, num2, num3):
    s = (num1 + num2 + num3) / 2 #calculating the semiperimeter

    area = (s * (s - num1) * (s - num2) * (s - num3)) ** 0.5
    return area


area = calc_area(5, 3, 4)
print( area)



