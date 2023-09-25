def showProgramName( ) :
    print( '**-- โปรแกรมคำนวณค่าคอมมิชชั่นของพนักงานขาย --**')

def inputData( ) :
    employeeId = input('ป้อนรหัสของพนักงาน : ')
    name = input('ป้อนชื่อของพนักงาน : ')
    money = float(input('ป้อนยอดขายของพนักงาน : '))
    return employeeId, name, money

def commission( money) :
    if money <= 1000 :
       total =  0
    elif money < 1000 >= 2000 :
        total = money * 0.01
    elif money < 2000 >= 3000 :
        total = money * 0.03
    else :
        total = money * 0.05 
    return total

def   showCommission(total) :
    print(f'ค่าคอมมิชชั่น เทากับ {total:.2f} บาท' )

showProgramName( )
print('--------------------------------------')
employeeId, name, money = inputData()
print('--------------------------------------')
showCommission(commission( money))
print('--------------------------------------')