def showProgramName( ) :
    print( '**-- โปรแกรมตรวจสอบผลการเรียนของนักเรียน--**')

def inputData( ) :
    student = int(input('ป้อนจำนวนนักเรียนที่จะตรวจสอบ : '))
    return student

def inputstudent( ) :
    studentId = int(input('ป้อนรหัสนักเรียน : '))
    name = input('ป้อนชื่อนักเรียน : ')
    average = float(input('ป้อนเกรดเฉลี่ยนของนักเรียน : '))
    return studentId, name, average

def result(average) :
    if average < 2 : 
        result = "สอบไม่ผ่าน"
    else :
       result = "สอบผ่าน"
    return result

def showAverange( result ) :
    print(f'ผลการเรียนของนักเรียน คือ : {result} ' )

showProgramName( )
print('--------------------------------------')
student = inputData( )
print('--------------------------------------')
studentId, name, average = inputstudent( )
print('--------------------------------------')
showAverange( result(average))
print('--------------------------------------')