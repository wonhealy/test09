import sys
sys.setrecursionlimit(10*8)
#
# def hundred(x):
#     for i in range(x,x-1):
#         sum+=1
#     return sum
#
# def recur(x):
#     if x == 1:
#         return 1
#     return x + recur(x-1)
#
# print(recur(100))
# import sys
#
# sys.setrecursionlimit(10*8)

# ********* 재귀함수 factorial***************
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


result = factorial(5)
print(result)


