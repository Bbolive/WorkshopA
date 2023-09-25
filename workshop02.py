def showProgramName( ) :
    print( '**-- โปรแกรมหาค่าเฉลี่ยของคะแนน --**')

def inputStudent( ) :
    password = input('ป้อนรหัสนักศึกษา : ')
    name = input('ป้อนชื่อนักศึกษา : ')
    score1 = float(input('ป้อนคะแนนสอบครั้งที่ 1 : '))
    score2 = float(input('ป้อนคะแนนสอบครั้งที่ 2 : '))
    score3 = float(input('ป้อนคะแนนสอบครั้งที่ 3 : '))
    return password, name, score1, score2, score3

def calAverangeScore( score1, score2, score3 ) :
    averange_score =  (score1 + score2 + score3) / 3
    return averange_score

def showProgramAverage( password, name, score1, score2, score3, averange_score ) :
    print(f'รหัสนักศึกษา {password}')
    print(f'ชื่อนักศึกษา {name}')
    print(f'คะแนนสอบครั้งที่ 1 {score1}')
    print(f'คะแนนสอบครั้งที่ 2 {score2}')
    print(f'คะแนนสอบครั้งที่ 3 {score3}')
    print(f'ค่าเฉลี่ย {averange_score:.2f}')

showProgramName( )
print('--------------------------------------')
password, name, score1, score2, score3 = inputStudent()
print('--------------------------------------')
averange_score = calAverangeScore( score1, score2, score3 )
print('--------------------------------------')
showProgramAverage( password, name, score1, score2, score3, averange_score )
print('--------------------------------------')