# class Menu:
#     def __init__(self): # 생성자
#         # self.name = []
#         # self.price = []
#         self.menuList =[]
#         self.build()
#
#     def build(self):
#         f = open("C:/Users/1234/Documents/menu.txt",'r')
#         arMenu = f.readlines()
#         for x in arMenu:
#             ar = x.split(",")
#             self.menuList.append({'name': ar[0],'price': int(ar[1])})
#         f.close()
#
#     def save(self):
#         # self.menuList의 내용을 menu.txt파일에 저장()
#     def add(self):
#         pass
#
#     def display(self):
#         for x in self.menuList:
#             print(f"{n:2d}.{x['name']:10s},{x['price']:5d}")
#             n+=1
#     def update(self):
#         pass
#
#     def delete(self):
#         pass
# self.menuList의 내용을 menu.txt화일에 저장(f.writeLine(str))






 # '메뉴명을 입력하시오'출력
        # input으로 메뉴명 읽어들이기
        # 메뉴명이 빈문자열이 아닌 동안
        # 가격 읽어 들이기
        # self.menuList에  메뉴명,가격추가
        # ' 메뉴명을입력하시오' cnffur
        # input으로 메뉴명 읽어들이기

# 수정할 메뉴번호 읽어들이기
        # 메뉴번호가 빈문자열이 아닌동안  pass
        # 메뉴명 읽기
        # 가격 읽기
        # 해당 메뉴번호의 메뉴명, 가격 update
        #(list[n]={'name':name,'price':price}
        # self.display()
        # 수정할 메뉴번호 읽어들이기

 # self.display()
        # 지울 메뉴번호 읽어들이기
        # 메뉴번호가 빈 문자열이 아닌동안,
        # DEL SELF.MENUlIST[n]
        # del self.menuList[n]
        # display()
        # 지울 메뉴번호 읽어들이기

def save(self):
    # self.menuList의 내용을 menu.txt파일에 저장()
    f = open("C:/Users/1234/Documents/menu.txt",'w')
    newline =''
    for x in self.menuList:
            line = newline+f"{x['name']},{x['price']}"
            f.write(line)
            newline ='/n'
    f.close()


def add(self):
    arMenu = []
    arPrice = []

    while True:
        menu = input("메뉴명을 입력하세요: ")
        if menu == "":
            break
        price = int(input("가격을 입력하세요: "))
        arMenu.append(menu)
        arPrice.append(price)

    for i in range(len(arMenu)):
        self.menuList.append({'name': arMenu[i], 'price': arPrice[i]})

    print("메뉴명 가격 목록: ")
    for i in range(len(arMenu)):
        print(f'{arMenu[i]} {arPrice[i]}')

    totalPrice = sum(arPrice)
    print("전체 가격 합계: ", totalPrice)
    self.save()

def update(self):
    self.display()
    menu_idx = input("수정할 메뉴 번호를 입력하세요: ")
    while menu_idx != "":
        menu_idx = int(menu_idx) - 1
        if 0 <= menu_idx < len(self.menuList):
            menu_name = input("수정할 메뉴명을 입력하세요: ")
            menu_price = int(input("수정할 가격을 입력하세요: "))
            self.menuList[menu_idx]['name'] = menu_name
            self.menuList[menu_idx]['price'] = menu_price
            self.display()
        menu_idx = input("수정할 메뉴 번호를 입력하세요: ")
    self.save()

def delete(self):
    self.display()
    menu_idx = input("지울 메뉴 번호를 입력하세요: ")
    while menu_idx != "":
        menu_idx = int(menu_idx) - 1
        if 0 <= menu_idx < len(self.menuList):
            del self.menuList[menu_idx]
            self.display()
        menu_idx = input("지울 메뉴 번호를 입력하세요: ")
    self.save()




