# i, j, k, str1 =0, 1, 3.14, 'Hellow world'
# print("i["+str(1)+"] j ("+str(j)+"] str1 ["+str1+"]")
# print(f'i [{i}] j [{j}] k[{k}] str1 [{str1}]')
# print(f"i {i:2d} j {j:3d} k{k:4.2f} str1={str1:12s}")
# print('i={1}, j={0}, k={3} str1={2}'.format(i,j,k,str1))
#
# f = open("C:/Users/1234/Documents/menu.txt")
# str1 = f.readline()
# print(str1, end='')
# str1 = f.readline()
# print(str1, end='')
# str1 = f.readline()
# print(str1, end='')
# str1 = f.readline()
# print(str1, end='')
# str1 = f.readline()
# print(str1, end='')
# str1 = f.readline()
# print(str1, end='')
# str1 = f.readline()
# print(str1, end='')
# f.close()
# f-String
# print(f'i={i:d},j={j:2d} ,str1={str1:12s}')
# format()
# print('i={0},j={1},str1={2}'.format(i,j,str1))
# %
# print)('i')

# for i in range(10): # 0~9
#  print(i)
#
# for i in range(1,10):
#  for j in range(1, 10):
# # print(f'{i} * {j}  = {i*j} ')
# for i in range(2, 10):
#     for j in range(1, 10):
#         print(f'{i} * {j} = {i*j}')
# for i in range(2,10): //구구단
#     for j in range(1,10):
#         print(f'{i}*{j}={i*j}')

# //몫 , **거듭제곱


#
# i = 9//3
# j= 9%3
# print(i)
# print(j)
# a= 2**4
# print(a)

# i++ , ++i, i-- 증감연산자 없음
# ==, != , >, < , <= --자바 자바스크립트 와 동일

# i = 2
# j = 2.0
# k= 3.14
# m='240'
# print(i==j)  # 파이썬은 결과값이 앞자리 대문자로 나옴!
# print(float(i),int(j), str(i),str(j),int(k)) # 정수 소수를 변형하기
# print(int(m), float(m)) # type변형하기

# 파이썬은'null'없고 'None'으로 쓰임

# d= 89000
# n= 751000
# total = d * 100 + n * 20
# print(total)
#
#
# a= d*0.05*100
# b= n*0.1*20
# c=a+b
# print(c)
#
# c = (50-32)/1.8
# print(c)
# i=11
# if i<10:
#    print('참입니다.')
#
# else:
#     print("거짓입니다.")
#
# price =7000
# if price<1000:
#     bid =1
# elif price >= 1000 and price<5000:
#     bid =5
#
# elif price >= 5000 and price <10000:
#     bid =50

# 1부터 100까지 홀수 출력
# (1) range()
# (2) if 로 체크

# for i in range(1,101,2):
#  print(i)
#
# for num in range(1,101):
#  if num % 2 != 0:
#   print(num)
#
# for i in range(1,102,3):
# #     print(i)
#
# fruits =[ 'orange','apple','pear','banana','kiwi','apple','banana','apple']
# print(fruits[:4])




# fruits.index('banana')
# fruits.index('banana',4)
#
# money =1000
# while money <3000:
#     money = money +500
#     inf money >=3000:
#     print("지금 가진 돈이 ")
#     print("용돈을 받아서 현재 가진 돈은 ,money, 입니다.")

# name =input('이름을 입력하시오:')
# print('이름:',name)
#
# for i in range(2,10):
#     for j in range(1,10):
#         print(f'{i}x{j}={i * j}')




  # -- 1000 이하의 소수 (Prime Number) 구하기

#   a = 1
#   b= 1000
#   c
#
#
# a = 8
# for i in range(a):
#   print(i)
#
# a = 10
# for i in range(a):
#  print(('*' * (i+1))
#
#
# def is_prime(i):
#     for num in range(2, i + 1):
#         if num % i == 0 and num != i:
#   print(i)
#
# a = 20
# for i in range(a):
#     print('*'*(i+1))
# for i in range(a - 1):
#     print('*'*(i))
#
#
# for i in range(5):
#     for j in range(i+1):
#         print('*',end="")
#         print("")
# i = 20
# for j in range(1,i,2):
#     print(j*"*")
# for j in range(i,0,-2):
#     print(j*'*')


# for i in range (4,1001):  // 1~1000 소수 구하기
#     for j in range(2,i):
#         if i%j == 0:
#             break
#     if j == i-1:
#         print(i)

# for i in range(4, 1001):  // 1~1000소수 구하기
#     for j in range(2, 1):
#         if i % j ==0:
#          break
#     else:
#         print(i)

# 최대 공약수/ 최소 공백수 구하기
# a = input("두 수중 작은 수를 찾아라")
# print("최대공약수:" + a)
# 1. 두 수중 작은수를 찾는다
# 2. 2~ (작은수 -1)= x 반복하면서 부른다
# 나눠지지 않으면 x를 증가
#
# 나눠지면 x값 보관 a <--a b<-- b

# 최대공약수 공배수
# def maxN(a, b):
#     while b != 0:
#         a, b = b, a % b
#     return a
#
# def minN(a, b):
#     return abs(a * b) // maxN(a, b)
#
# # 사용자로부터 두 개의 정수 입력 받기
# a = int(input("첫 번째 정수를 입력하세요: "))
# b = int(input("두 번째 정수를 입력하세요: "))
# #두 수 중 작은 수 찾기
# min_value = min(a, b)
#
# # 최대공약수 계산
# maxNo = maxN(a, b)
# # 최소공배수 계산
# minNo = minN(a, b)
#
# # 결과 출력
# print("최대공약수:", maxNo)
# print("최소공배수:", minNo)

# for i in range(0, 3, 1):
#     print("안녕하세요?for 문을 공부중입니다.")

# for i in [0 , 1,2]:
#     print("나는 이거 쉬워")
#
# aa= []
# for i in range(0, 100):
#     aa.append(0)
#     len(aa)
#     print(aa)
#
#
# def order():
#     print('주문 하실 음료를 알려 주세요')
#     drink = input()
#     print(drink, '주문하셨습니다.')
#
# order()
#
#
#
# def print_absolute():
#     print('정수를 입력하세요')
#     a=(int(input())
#     print('-15의 절대값:' , a )

# a,b,c,값을 읽어서 이차방정식의 근(해)를 구하기


# -- 이차방정식의 근(해)을 구하는 함수 정의 & 호출
import math
# def solve_quadratic_equation():
#     while True:
#         try:
#             a = float(input("계수를 입력하세요 : "))
#             break
#         except ValueError:
#             print("유효하지 않습니다. 다시 입력해주세요")
#
#     while True:
#         try:
#             b = float(input("Enter the coefficient b: "))
#             break
#         except ValueError:
#             print("Invalid input. Please try again.")
#
#     while True:
#         try:
#             c = float(input("Enter the coefficient c: "))
#             break
#         except ValueError:
#             print("Invalid input. Please try again.")
#
#     discriminant = b**2 - 4*a*c
#
#     if discriminant > 0:
#         # 두 개의 실근을 가지는 경우
#         root1 = (-b + math.sqrt(discriminant)) / (2*a)
#         root2 = (-b - math.sqrt(discriminant)) / (2*a)
#         return root1, root2
#     elif discriminant == 0:
#         # 중근을 가지는 경우
#         root = -b / (2*a)
#         return root
#     else:
#         # 허근을 가지는 경우
#         real_part = -b / (2*a)
#         imaginary_part = math.sqrt(-discriminant) / (2*a)
#         complex_root1 = complex(real_part, imaginary_part)
#         complex_root2 = complex(real_part, -imaginary_part)
#         return complex_root1, complex_root2
#
# # 함수 호출
# roots = solve_quadratic_equation()
#
# if isinstance(roots, complex):
#     print("이차방정식은 허근을 가집니다.")
#     print("복소근 1:", roots[0])
#     print("복소근 2:", roots[1])
# elif isinstance(roots, tuple):
#     if len(roots) == 1:
#         print("이차방정식은 중근을 가집니다.")
#         print("중근:", roots[0])
#     else:
#         print("이차방정식은 실근을 가집니다.")
#         print("실근 1:", roots[0])
#         print("실근 2:", roots[1])


import math

x=1
y=2
x,y =y,x
print(x,y)
def solve1(a,b,c):
    x = b ** 2-4 * a * c
    if x<=0 :
        return 0, 0
        x1 = (b + math .sqrt(x))/(2 * a)
        x2 = (b - math. sqrt(x))/(2 * a)
        return x1,x2


    a , b  = solve(1, -3 , 2)

    print('x1=',a,'\nx2=',b)




































