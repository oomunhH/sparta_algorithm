input = [0, 3, 5, 6, 1, 2, 4]


def find_max_plus_or_multiply(array):
    multiply_sum=0
    for element in array:
        if multiply_sum==0 or element<=1:
            multiply_sum+=element
        else:
            multiply_sum*=element
    return multiply_sum


result = find_max_plus_or_multiply(input)
print(result)

#페이스북 기출문제!!