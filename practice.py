def open_account():
    print("새로운 계좌가 생성되었습니다.")
def deposit(balance, money):
    print("입금이 완료되었습니다.잔액은 {0}원 입니다. ".format(balance+money))
    return balance +money

def withdraw(balance, money):# 출금

balance = 0 # 잔액
balance = deposit(balance,1000)
print(balance)