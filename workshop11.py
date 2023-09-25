def showProgramName( ) :
    print( '**-- โปรแกรมคำนวณค่าโทรศัพท์ --**')

def inputData( ) :
    name = input('ป้อนชื่อผู้ใช้โทรศัพท์ : ')
    phoneNumber = int(input('ป้อนหมายเลขโทรศัพท์ : '))
    minute = float(input('ป้อนจำนวนนาทีที่ใช้ทางโทรศัพท์ : '))
    return name, phoneNumber, minute

def calBill( minute) :
    if minute <= 15 :
        min = minute * 5
    elif minute >= 16 <= 30 :
        min = minute * 3
    else :
        min = minute * 1.5
    return min

def showBill(min) :
    print(f'ค่าโทรศัพท์ทั้งหมด คือ : {min:.2f} บาท' )

showProgramName( )
print('--------------------------------------')
name, phoneNumber, minute = inputData( )
print('--------------------------------------')
showBill( calBill( minute))
print('--------------------------------------')