def showProgramName( ) :
    print( '**-- โปรแกรมคำนวณหาเงินเดือนสุทธิของพนักงาน --**')

def inputData( ):
    password = int(input('ป้อนรหัสพนักงาน '))
    name = input('ป้อนชื่อพนักงาน ')
    money = int(input('ป้อนเงินเดือนปกติของพนักงาน '))
    return password, name, money

def calMoneyVat( money ) :
    money_vat = money * 0.07
    return money_vat

def calMoneySocialSecurity( money ) :
    money_social_security = money - 500
    return money_social_security

def Net( money_vate, money_social_security) :
    net = money_social_security - money_vate
    return net

def showNetSaraly( money_vat, net) :
    print(f'ภาษี : {money_vat:.2f} บาท\nเงินเดือน : {net} บาท')

showProgramName( )
print('--------------------------------------')
password, name, money = inputData()
print('--------------------------------------')
showNetSaraly( calMoneyVat( money ), Net( calMoneyVat( money ), calMoneySocialSecurity( money )))
print('--------------------------------------')