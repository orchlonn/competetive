# def product_digits(a):
#     return (a % 10) * (a // 10)

# print(product_digits(77)


# def sum_digits(a):
#     last_digit = a % 10
#     a = a // 10
#     middle_digit = a % 10
#     first_digit = a // 10
#     sum = last_digit + middle_digit + first_digit
#     return sum

# def sum_digits(a):
#     last_digit = a % 10
#     a = a // 10
#     middle_digit = a % 10
#     first_digit = a // 10
#     sum = last_digit + middle_digit + first_digit
#     return (a % 10) + (a // 10) + (a // 10 % 10)

# def sum_digits(a):
#     return (a % 10) + (a // 10 % 10) + (a // 10 // 10)

# def convert_seconds(s):
#     return [s // 60, s % 60]

# print(convert_seconds(200))

# # solution: 1
# def greatest_number(a ,b):
#     if a < b:
#         greatest_number = b
#     else: 
#         greatest_number = a
#     return greatest_number

# print(greatest_number(14, 2))

# # Solution: 2
# def greatest_number(a, b):
#     if a < b:
#         return b
#     else:
#         return a

# Solution: 3
# def greatest_number(a, b):
#     greates_number = max(a, b)
#     return greates_number

# Solution: 4
# def greatest_number(a, b):
#     greatest_number = a if a > b else b
#     return greatest_number

# def greatest_number_three(a,b,c):
#     if a < b:
#         if c < b:
#             return b
#         else: 
#             return c
#     elif c < a:
#         return a
#     else:
#         return c 
    

# def even_num(a,b,c):
#     sum = 0
#     if a % 2 == 0:
#         sum = sum + a
#     if b % 2 == 0:
#         sum = sum + b
#     if c % 2 == 0:
#         sum = sum + c
        
#     return sum

# print(even_num(2,3,12))


# def seconds_converter(a):
#     hours = 0
#     minutes = 0
#     if(a // 3600 > 0):
#         hours = a // 3600
#         a = a - hours * 3600
#     if(a // 60 > 0):
#         minutes = a // 60
#         a = a - minutes * 60

#     seconds = a
    
#     return [hours, minutes, seconds]

# print(seconds_converter(1721))

# def hours_converter(hours):
#     return [hours // 24, hours - (hours // 24) * 24]

# print(hours_converter(70))

# def convert_to_hours(days, hours):
#     total_hours = days * 24 + hours
#     return total_hours

# print(convert_to_hours(2, 5))
# def convert_months(months):
#     return months // 12, months - (months // 12 * 12)

# print(convert_months(22))

# def lowest_number(a,b,c,d):
#     if a > b:
#         if a > c:
#            if a > d:
#                return a
#            else:
#                return d
#         elif c > d:
#             return c
#         else:
#             return d
#     elif b > c:
#         if b > d:
#             return b
#         else:
#             return d
#     elif c > d:
#         return c
#     else:
#         return d
    
# print(lowest_number(112,222,13,412))   

# def n_times(s, n):
#     total =  s if n == 1 else 0
#     for i in range(1,n):
#         total += s        

#     return total

# print(n_times(3, 1))

# def n_power_2(n):
#     return 2 ** n
# print(n_power_2(4))

# def n_power_a(a, n):
#     return a ** n

# print(n_power_a(2, 5))

# def criteria_level(gpa):
#     if(gpa == 4):
#         return "Excellent"
#     elif(gpa >= 3):
#         return 'Good'
#     elif(gpa >= 2):
#         return 'Nod bad'
#     else:
#         return "Worst"
    
# print(criteria_level(4))

# def week_number_text(day):
#     if day == 1:
#         return 'Monday'
#     elif day == 2:
#         return 'Tuesday'
#     elif day == 3:
#         return 'Thursday'
#     elif day == 4:
#         return 'Wednesday'
#     elif day == 5:
#         return 'Friday'
#     elif day == 6:
#         return 'Saturday'
#     else:
#         return 'Sunday'

# print(week_number_text(4))

# def month_to_season(month):
#     if (month  == 1 or month == 12 or month == 11):
#         return "Winter"
#     elif (month == 2 or month == 3 or month == 4):
#         return "Spring"
#     elif (month == 5 or month == 6 or month == 7):
#         return "Summer"
#     else:
#         return "Fall"

# print(month_to_season(3))

# def isosceles_triangle_checker (a,b,c):
#     if (a + b > c and b + c > a and a + c > b):
#         return "YES"
#     else:
#         return "NO"

# def isosceles_triangle_checker(a, b, c):
#     return "YES" if(a + b > c and b + c > a and a + c > b) else "NO"
# print(isosceles_triangle_checker(33,19,5))

# def easy_expression(a, b, c):
#     return  a * b - c


# print(easy_expression(5,6,14))

# import bisect 

# def determine_grade(scores, breakpoints=[50, 60, 70, 80, 90], grades='FEDCBA'):
#     i = bisect.bisect(breakpoints, scores)
#     return grades[i]

# print(determine_grade(88))

# def float_converter(a):
#     return int(a)

# print(float_converter(32.21321))

# def int_to_string(a):
#     return str(a)

# def float_to_string(a):
# #     return str(a)

# def add_two_string(a, b):
#     return str(a) + str(b)

# print(add_two_string(2,-32))

# def split_string(a):
#     result = a.split()
#     return result
# print(split_string('hello world'))

# def vowel_counter(s):
#     counter = s.lower().count("i")
#     return counter

# print(vowel_counter("I love sushi."))

# def lower_case_string(str):
#     return str.lower()

# def lower_case_string(str):
#     lower_str = str.lower()
#     return lower_str

# def upper_case_string(str):
#     uppercase_str = str.upper()
#     return uppercase_str

# print(upper_case_string('hello, tokyo'))

# def detect_upper_str(str):
#     return  str.isnumeric()
    

# print(detect_upper_str("123"))

# def slicing_left_indices(text):
#     sliced_text = text[-8:-5]
#     return sliced_text
# print(slicing_left_indices("Life Doesn’t Frighten Me"))
# import math
# print(-7 * - 7)   

# def sortedSquares(nums):
        
#     for i in range(len(nums)):
#         nums[i] = nums[i] * nums[i]
#     nums.sort()
    
#     return nums

# print(sortedSquares([-4,-1,0,3,10]))


# from math import e, log

# def sqrt_number(x):
#     if x < 2:
#         return x
#     left = int(e**(0.5 * log(x)))
#     right = left + 1
#     return left if right * right > x else right

# print(sqrt_number(14))

# def sqrt_number( x):
#     if x < 2:
#         return x
        
#     left, right = 2, x // 2

        
#     while left <= right:
#         pivot = left + (right - left) // 2
#         num = pivot * pivot
        
#         if num > x:
#             right = pivot -1
#         elif num < x:
#             left = pivot + 1
#         else:
#             return pivot
            
#     return right
    
# print(sqrt_number(14))

def isPalindrome(num):
    if num < 0:
        return False
    rev = 0
    orig = num
    while num != 0:
        rev = rev * 10 + num % 10
        num //= 10
    return rev == orig
            
print(isPalindrome(121))