#Write a function that accepts four values, it sums up the first two values, multiplies by the third value and divides the result by the fourth value

def complex_cal(a,b,c,d):
    cal_sum = a + b
    cal_mul = cal_sum * c
    final_cal = cal_mul / d

    return final_cal


print(complex_cal(20,30,2,4))