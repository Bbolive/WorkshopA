def showProgramName( ) :
    print( '**-- โปรแกรมตรวจสอบค่า pH --**')

def inputData( ):
    name = input('ป้อนชื่อจังหวัด : ')
    pH = float(input('ป้อนค่า pH : '))
    return name, pH

def amountPh( pH ) :
    if pH >  8 :
        result = 'Result is Acid'
    elif pH < 8 :
        result = 'Result is Alkali'
    else:
       result = 'Result is Normal'
    return result

def showPh( result ) :
    print(f'{result}')

showProgramName( )
print('--------------------------------------')
name, pH = inputData( )
print('--------------------------------------')
showPh(amountPh( pH ) )
print('--------------------------------------')