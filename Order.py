import Menu

class Order(menu.Menu):
    def __init__(self):
        #orderList 안에 들어가는 딕셔너리는 세가지 정보를 포함한다
        #메뉴명,수량,총액
        self.orderList = []
    def add(self):
        pass
        # 메뉴목록을 보여준다
        # 주문할 메뉴번호를 입력받는다('':종료)
        # 수량을 입력받는다
        #총액은 계산/표시
        #orderList에 추가

    def display(self):
        pass
        # 주문내역을 보여준다

    def display(self):
        pass
    #메뉴목록을 보여준다
    #삭제할 주문번호를 입력받는다('':종료)
    #orderList에 삭제(주문번호-1해야 지울 주문의 인덱스가 구해짐)

    def delete(self):
        pass