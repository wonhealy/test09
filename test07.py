import os
import glob
#
# print(os.getcwd())
# os.chdir('c:/PythonStudy')
# print(os.getcwd()) # get Current Working Directory
#
# print(glob.glob('*'.'py'))   # ---파일 목록에 뭐가 있는지 볼때 불러들이는코드

# import random
# #
# # print(random.choice['John','Jane','James','Johanson','Joey',])
# print(random.sample(range(1,45) ,6),'+',random.sample(range))
#
#**************date hour******************
# from datetime import date, datetime
# now = datetime.now()
# print(now)
# print(now.strftime("%y/%m/%d %H:%M:%S"))
# from datetime import date, datetime
# now = datetime.now()
# print(now)
# print(now.strftime("%Y/%M/%D %H:%M:%S"))
# *************************주민번호***********
# pid=input('주민번호를 입력하시오')
# n=2
# sum=0
# str1=''
# for i in pid[:-1]:
#     sum+=int(i)*n
#     if str1!='':
#         str1+='+'
#     str1+=i+'x'+str(n)
#     n+=1
#     if n>9:
#         n=2
# print(11-sum%11,',',pid[-1])
# print(str1)



for num in range(2, 10):
    if num % 2 == 0:
        print("even",num)
        continue
    print( "odd", num)
