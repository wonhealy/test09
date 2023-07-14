import re # regular Expression module import!
def checkEmail(email):
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,7}\b'
    # regex = /\b[A-Za-z0-9],_%+-]+@[A-Za-z0-9,-]+\.[A-Z|a-z]{2,7}\b/;
    if (re.fullmatch(regex, email)):
        return True
    else:
        return False
# 정규표현식
def checkMobile(mobile):
    regex = "(\+\d{1,3})?\s?\(?\d{1,4}\)?[\s.-]?\d{3}[\s.-]?\d{4}"
    if(re.fullmatch(regex,mobile)):
        return True
    else:
        return False

phone = input('모바일번호를  입력하시오')
if checkMobile(phone):
    print('유효한 모바일번호입니다.')
else:
    print('존재할 수 없는 모바일번호입니다')
# userid = input('email주소를 입력하시오)
