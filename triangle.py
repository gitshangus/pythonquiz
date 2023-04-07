def triangle(a, b):
    area = (a * b)/2
    return area


num = input('밑변과 높이를 입력하시오.').split()
num1 = int(num[0])
num2 = int(num[1])

d = triangle(num1, num2)
print(d)