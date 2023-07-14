#Create(add)
# arName =[1, 'Hello', 3.14,True, None,"World"]
#
# arName.append(25)
# arName.insert(3,'이원정')
# #read
# for x in arName:
#     print(x)
#
# for i in range(len(arName)):
#     print(i, '=',arName[i])

# print('0',arName[0])
# print('1',arName[1])
# print('2',arName[2])
# print('3',arName[3])
# print('4',arName[4])
# print('5',arName[5])
# print('6',arName[6])
# print('7',arName[7])
# x = arName[3]
# print(type(x))
#Update
# arName[3] = '하이미디어'
# print('-'*30)
# for x in arName:
#     print(x)
#
# #Delete
# arName.remove('하이미디어')
# print('-'*30)
# for x in arName:
#     print(x)


# del arName[3] #인덱스로 지우기
#
# x = arName.pop(3)
#
# arName.clear()
# arName.sort()
# arName.reverse()



# arList = [1, 3, 5, 7, 8, 11, 13, 15, 17]
# arList[0], arList[8], arList[1],arList[7],arList[2],arList[6],arList[3],arList[5] = \
#     arList[8], arList[0],arList[7],arList[1],arList[6],arList[2],arList[5],arList[3]
# print(arList)
# newNum =arList.pop(0)
# arList.insert(17, newNum)
# print(arList)
#
# newNum =arList.pop(8)
# arList.insert(15, newNum)
# print(arList)
# arList = [1, 3, 5, 7, 8, 11, 13, 15, 17]
# i = 0
# j = len(arList)-1
# while i<j:
#     arList[i],arList[j] =arList[j],arList[i]
#     i+=1
#     j-=1
# print(arList)
#
#
# arTemp =[]
# for i in range(len(arList)-1,-1,-1):
#     arTemp.append(arList[i])
#     arList.clear()
# for x in arTemp:
#         arList.append(x)
# print(arList)
#


# -- Menu명이 빈문자열이 입력될 때까지, MenuList를 작성 & 메뉴명/가격 목록 출력
# arMenu =[]
# arPrice =[]
#
# while True:
#     menu = input("메뉴명을 입력하세요: ")
#     if menu == "":
#         break
#     price = int(input("가격을 입력하세요: "))
#     arMenu.append(menu)
#     arPrice.append(price)
#
# print("메뉴명  가격 목록:")
# for i in range(len(arMenu)):
#     print(f"{arMenu[i]} {arPrice[i]}")
#
# #-- 모든 메뉴의 가격 합계
# Totalprice = sum(arPrice)
# print("전체 가격 합계:", Totalprice)
#----------------------------------------------------------------------------------
# 1. menu, price
# 2. dictionary
# 3. append 사용해서 list 에 추가


menuList = []

while True:
    menu = input("메뉴명을 입력하세요: ")
    if menu == "":
        break
    price = int(input("가격을 입력하세요: "))
    menuList.append( {'name':menu, 'price':price} )

for menu in menuList:
    print("{}의 가격은 {}입니다.: ".format(menuList['menu'],menuList['price']))


# print("메뉴명 가격 목록:")
# totalPrice = 0
# for menu in menuList:
#     if menu in menu:
#         price = menu[menu]
#         print(f"{menu} {price}")
#         totalPrice += price
#     else:
#         print(f"{menu}은(는) 메뉴에 없습니다.")
#
# print(f"모든 메뉴의 가격 합계: {totalPrice}")


arMenu = []
arPrice = []

while True:
    menu = input("메뉴명을 입력하세요: ")
    if menu == "":
        break
    price = int(input("가격을 입력하세요: "))
    arMenu.append(menu)
    arPrice.append(price)
print("메뉴명 가격 목록: ")


for i in range(len(arMenu)):
    print(f'{arMenu[i]} {arPrice[i]}')

totalPrice = sum(arPrice)
print("전체 가격 합계: ", totalPrice)
#
# s1={1,2,3,4,5,6}
# s2={5,6,7,8,9,10}
# s3=s1.union(s2)
# print(s3)




















