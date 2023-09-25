def showProgramName( ) :
    print( '**-- โปรแกรมแสดงข้อความต้อนรับนักศึกษา --**')

def inputData(  ) :
    yearStudent = int(input('ป้อนชั้นปีการศึกษา : '))
    return yearStudent

def massage( yearStudent ) :
    if yearStudent == 1 :
        massage = "Welcome Freshman"
    elif yearStudent == 2 :
        massage = "Welcome Sophomore"
    elif yearStudent == 3 : 
        massage = "Welcome Junior"
    else :
        massage = "Welcom Senior"
    return massage

def showMassage( massage ) :
    print(f'{massage}' )

showProgramName( )
print('--------------------------------------')
yearStudent = inputData( )
print('--------------------------------------')
showMassage( massage( yearStudent ) )
print('--------------------------------------')