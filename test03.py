# def Prime():
#     arPrime =[]
#     for i in range(1000):
#         for j in range(2, i):
#             if i % j == o: break
#         else:
#             arPrime
#
# d1 ={3.14:'Pi','e':1.023}
# print(d1)
# print('3.14','e')
# print(d1[3.14])
# print(d1['e'])
# d2 = { 'name': 'John' , 'age':23, 'city':'Goyang','birthday':'20030617', 20:'20"s'}
# for x in d2:
#     print(x,d2[x])
# print('-'*30)
# for k,v in d2.items():
#     print(k,v)


# print(d2[20])
# print(d2['name'])
# print(d2['age'])
# d3 ={'list': [1,2,3,4,5],'tuple':(1,2,3,4,5), 'set':{1,2,3,4,5},'dict':{'name':'Llsan','city':'Cheona'}}
# for x in d3:
#     print(x,d3[x])
# for i, a in  d3.items():
#     print(i,a)

# print(d3['list'])
# print(d3['tuple'])
# print(d3['set'])
# print(d3['dict']['name'])

 # l4 =[{'name': 'John', 'age': 23},{'name': 'jane', 'age': 20},{'name': 'Jason', 'age': 33}]
 # for x in l4:
 #     print(x['name'],x['age'])


menuList={'Latte': 3000, 'black': 2000,'cappucino': 3500,'Cocoa':2500,'Milkchoco':2500}
print(menuList.items())

# for menu,price in menuList.items():
#     print('{0}의 가격은 {price}입니다.'.format(menu,price))

total = 0
for i in menuList.values():
    print(i)
    total += i
print("totalPrice :{}".format(total))

for key, value in menuList.items() :
    print('{}의 가격은 {}입니다.'.format(key,value))














