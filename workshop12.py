def showProgramName( ) :
    print( '**-- โปรแกรมคำนวณค่าใช้จ่ายในการซื้อแพ็คเกจท่องเที่ยวของกรุ๊ปทัวร์ --**')

def inputData( ) :
    name = input('ป้อนชื่อหัวหน้ากรุ๊ปทัวร์ : ')
    phoneNumber = int(input('ป้อนหมายเลขโทรศัพท์ของหัวหน้ากรุ๊ปทัวร์ : '))
    people = int(input('ป้อนจำนวนคนที่จะไปทัวร์ : '))
    return name, phoneNumber, people

def bill( people ) :
    if people <=2 :
        total = 300
    elif people >=3 <=5 :
        total = 250
    elif people >=6 <=10 :
        total =  210
    else :
        total = 150
    return total

def showBill( total ) :
    print(f'ค่าใช้จ่ายในการซื้อแพ็คเกจท่องเที่ยวของกรุ๊ปทัวร์ คือ {people * total:.2f} บาท' )

showProgramName( )
print('--------------------------------------')
name, phoneNumber, people = inputData( )
print('--------------------------------------')
showBill( bill( people ))
print('--------------------------------------')