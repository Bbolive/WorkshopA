def showProgramName( ) :
    print( '**-- โปรแกรมคำนวณ Game Bingo --**')

def inputData( ):
    number = int(input('ป้อนตัวเลขที่ต้องการทาย : '))
    return number

def cal( number ):
    if number ==  25 :
        result = 'Correct, You are the winner'
    else:
       result = 'Not Correct!!!!!!'
    return result

def show ( result ) :
    print(f'{result}')

showProgramName( )
print('--------------------------------------')
number = inputData( )
print('--------------------------------------')
show(cal( number ))
print('--------------------------------------')