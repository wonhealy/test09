import Menu


menu =Menu.Menu() # Menu menu = new Menu();
menu.display() # menu.display();

# # 작업선택(m:메뉴관리. 0:주문관리, s:매출관리, " "/x:종료
#
# # M :
#     메뉴관리작업선택 (A: 추가, R:목록보기, U:수정, D:삭제, " ":메뉴관리)
#     if A:
#     elif R:
#     elif U:
#     elif D:
#     elif '':
#         break
#
# # 0 :
#     주문작업선택 0:주문하기, R:주문내역보기, '':주문관리종료)
#     if 0:
#     elif R:
#     elif " ":
#
# # s:
#      매출보기.


 # Menu 클래스의 인스턴스 생성

while True:
    choice = input("작업 선택 (M: 메뉴관리, 0: 주문관리, S: 매출관리, Enter/Space: 종료): ")

    if choice.upper() == "M":  # 메뉴관리 작업 선택
        while True:
            menu_choice = input("메뉴관리 작업 선택 (A: 추가, R: 목록보기, U: 수정, D: 삭제, Enter/Space: 메뉴관리 종료): ")

            if menu_choice.upper() == "A":  # 메뉴 추가
                menu.add()
            elif menu_choice.upper() == "R":  # 메뉴 목록 보기
                menu.display()
            elif menu_choice.upper() == "U":  # 메뉴 수정
                menu.update()
            elif menu_choice.upper() == "D":  # 메뉴 삭제
                menu.delete()
            elif menu_choice == "" or menu_choice.isspace():  # 메뉴관리 종료
                break

    elif choice == "0":  # 주문관리
        while True:
            order_choice = input("주문 작업 선택 (0: 주문하기, R: 주문내역 보기, Enter/Space: 주문관리 종료): ")

            if order_choice == "0":  # 주문하기
                # 주문하기 로직 추가
                pass
            elif order_choice.upper() == "R":  # 주문내역 보기
                # 주문내역 보기 로직 추가
                pass
            elif order_choice == "" or order_choice.isspace():  # 주문관리 종료
                break

    elif choice.upper() == "S":
        print("----- 매출보기 -----")
        total_sales = 0
        for sale in total_sales:
            print(f"메뉴: {sale['menu']} / 가격: {sale['price']}원")
            total_sales += sale['price']
        print("총 매출액:", total_sales)

    elif choice == "" or choice.isspace():  # 종료
        break


print('카페관리 프로그램 종료')