def showProgramName( ) :
    print( '**-- โปรแกรมคำนวณอัตราดอกเบี้ยเงินกู้ --**')

def inputData( ):
    name = input('ป้อนชื่อผู้กู้ : ')
    money = float(input('ป้อนจำนวนเงินกู้ : '))
    return name, money

def cal( money ):
    if money >=  1000 :
        interest = money * 0.025
    else:
        interest = money * 0.055
    return interest

def showInterest ( interest ) :
    print(f'อัตราดอกเบี้ยเงินกู้ : {interest:.2f} บาท')

showProgramName( )
print('--------------------------------------')
name, money = inputData( )
print('--------------------------------------')
showInterest(cal( money ))
print('--------------------------------------')